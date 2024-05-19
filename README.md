# Тестовое задание на вакансию: Разработчик в тестировании

# Описание задания тестирования [страницы](https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login) 
1) Авторизоваться пользователем «Harry Potter»;
2) Вычислить N-е число Фибоначчи, где N - это текущий день месяца + 1.
Пример: сегодня 08.02.2023, 9-е чисто Фибоначчи равно 21;
3) Выполнить пополнение счета (Deposit) на сумму равную вычисленному в
п.4 числу;
4) Выполнить списание со счета (Withdrawl) на сумму равную вычисленному
в п.4 числу;
5) Выполнить проверку баланса - должен быть равен нулю;
6) Открыть страницу транзакций и проверить наличие обеих транзакций;
7) Сформировать файл формата csv, в который выгрузить данные о
проведенных транзакциях;
Файл должен содержать строки следующего формата
<Дата-времяТранзакции Сумма ТипТранзакции>, где
Формат Дата-времяТранзакции - "ДД Месяц ГГГГ ЧЧ:ММ:СС"
Формат Сумма - число
Формат ТипТранзакции - значение из списка [Credit, Debit]
8) Оформить сформированный файл как вложение к отчету allure

# Allure отчет:
1) [Проверка баланса после пополнения и вывода депозита](https://github.com/BorisoffVlad/simbir_soft_test_task/blob/main/allure_report_screenshots/Screenshot_4.jpg)
2) [Проверка наполнения таблицы транзакциями после пополнения и вывода депозита](https://github.com/BorisoffVlad/simbir_soft_test_task/blob/main/allure_report_screenshots/Screenshot_5.jpg)

# Документация по локальному разворачиванию тестового окружения и запуска тестов
1) Склонировать репозиторий - < git clone https://github.com/BorisoffVlad/simbir_soft_test_task >
2) Развернуть сервер Selenium GRID - < java -jar selenium-server-4.21.0.jar standalone --config grid_config.json >
3) Запуск тестов с формированием allure-отчета - < pytest tests/test_transactions.py --alluredir=./allure-results > \
(опционально, можно добавить параметр < --headless=True > для запуска в headless-режиме)
4) Сформировать allure - отчет - < allure serve >
