import allure
import csv
import os


def create_csv_file_from_string(data_string):
    """
    Создает CSV-файл на основе строки данных.

    Аргументы:
        data_string (str): Строка данных, которая будет записана в CSV-файл.
         Данные должны быть представлены в формате таблицы, разделенной табуляцией,
          где первая строка представляет собой заголовки.

    Возвращает:
        str: Путь к созданному CSV-файлу.

    Вызывает исключение:
        Exception: Если произошла ошибка при генерации CSV-файла.

    Функция принимает строку данных, разбивает ее на список строк и затем разбивает первую строку на список заголовков.
     Затем вызывается функция `russify_headers` для перевода заголовков на русский язык.
      Остальные строки разбиваются на список строк данных.
       Затем открывается файл в режиме записи, создается объект CSV-записи,
       записываются переведенные заголовки в первую строку файла,
        а затем записываются строки данных в последующие строки. Наконец, возвращается путь к созданному CSV-файлу.

    Если произошла ошибка при генерации CSV-файла, вызывается исключение с сообщением об ошибке.
    """
    try:
        data_list = data_string.split("\n")
        eng_headers = data_list[0].split("\t")
        rus_headers = russify_headers(eng_headers)
        data = [line.split("\t") for line in data_list[1:]]

        file_path = "csv/transactions.csv"
        with open(file_path, mode="w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(rus_headers)
            writer.writerows(data)

    except Exception as e:
        raise Exception(f"Ошибка в генерации CSV файла: {e}")

    return file_path


def attach_csv_file_to_allure_report(data_string):
    """
    Прикрепляет CSV файл к отчету Allure.

    Аргументы:
        data_string (str): Строковое представление данных CSV.

    Эта функция создает CSV файл на основе заданной строки данных и прикрепляет его к отчету Allure.
    Она использует функцию `create_csv_file_from_string` для создания CSV файла.
    Функция считывает содержимое CSV файла и прикрепляет его к отчету Allure с помощью функции `allure.attach`.
    После прикрепления файла он удаляется из файловой системы с помощью функции `os.remove`.

    Примечание:
        Для использования этой функции необходимо установить модуль `allure`.
    Пример:
        attach_csv_file_to_allure_report("Name,Age\\nJohn,25\\nAlice,30")
    """
    with allure.step("Создаем CSV файл"):
        csv_file_path = create_csv_file_from_string(data_string)
        with open(csv_file_path, "rb") as file:
            allure.attach(
                file.read(),
                name="Таблица транзакций",
                attachment_type=allure.attachment_type.CSV,
            )
        os.remove(csv_file_path)


def russify_headers(header_list):
    """
    Генерирует новый список заголовков на русском языке на основе заданного списка заголовков на английском языке.

    Аргументы:
        header_list (List[str]): Список заголовков на английском языке.

    Возвращает:
        List[str]: Список заголовков на русском языке.

    Вызывает исключение:
        Exception: Если какой-либо заголовок не найден в списке ожидаемых заголовков.

    Пример:
        russify_headers(["Date-Time", "Amount", "Transaction Type"])
        ["Дата-времяТранзакции", "Сумма", "ТипТранзакции"]
    """
    new_header = []
    for i in header_list:
        try:
            match i:
                case "Date-Time":
                    new_header.append("Дата-времяТранзакции")
                case "Amount":
                    new_header.append("Сумма")
                case "Transaction Type":
                    new_header.append("ТипТранзакции")
        except Exception as e:
            print(
                f"{i} - отсутствует в списке ожидаемых заголовков. Текст ошибки: {str(e)}"
            )
    return new_header
