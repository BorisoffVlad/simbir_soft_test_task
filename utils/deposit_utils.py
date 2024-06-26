import datetime


def get_today_date():
    """
    Возвращает дату текущего дня в виде целого числа.
    """
    return int(datetime.datetime.now().day)


def fibonacci_list(today_date: int):
    """
    Генерирует последовательность Фибоначчи до указанной даты.
    Параметры:
        today_date (int): Дата, до которой нужно сгенерировать последовательность Фибоначчи.

    Возвращает:
        list: Список, содержащий последовательность Фибоначчи до указанной даты.
    """
    list_length = today_date + 1
    fib_list = [0, 1]
    while len(fib_list) < list_length:
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list


def get_deposit():
    """
    Получить сумму депозита на основе текущей даты.
    Эта функция вычисляет сумму депозита на основе текущей даты.
    Сначала она вызывает метод `get_today_date`, чтобы получить текущую дату в виде целого числа.
     Затем она вызывает метод `fibonacci_list` с текущей датой в качестве аргумента,
      чтобы сгенерировать последовательность Фибоначчи до текущей даты.
       Наконец,
        она возвращает последний элемент сгенерированной последовательности Фибоначчи в качестве суммы депозита.

    Возвращает:
        int: Сумма депозита на основе текущей даты.
    """
    serial_number = get_today_date()
    deposit = fibonacci_list(serial_number)[-1]
    return deposit
