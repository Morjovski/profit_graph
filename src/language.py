def choose_language():
    while True:
        lang = input('Choose a language\nВыберите язык\nОберіть мову\nEN/RU/UA: ')
        if lang.lower() == 'en' or len(lang) == 0:
            return "EN"
        elif lang.lower() == 'ru' or lang.lower() == 'кг':
            return "RU"
        elif lang.lower() == 'ua' or lang.lower() == 'гф':
            return "UA"
        else:
            print('Incorrect lang select!\nВведены неправилные данные!\nВведено неправильні дані!')

interval_mode_lang = {
    "EN": "Build graph by:\nYears at all - (1)\nYear by months - (2)\nMonths by days - (3)",
    "RU": "Просмотр графика за:\nЗа года в общем - (1)\nЗа года помесячно - (2)\nЗа месяцы по дням - (3)",
    "UA": "Дивитись графік за:\nЗа роки в цілому - (1)\nЗа роки помісячно - (2)\nЗа місяці по днях - (3)"
}

interval_mode_input_lang = {
    "EN": "Enter interval mode: ",
    "RU": "Введите режим: ",
    "UA": "Введіть режим: "
}

input_mode_lang = {
    "EN": "Enter data (1)\nBuild a graph (2): ",
    "RU": "Ввод прибыли (1)\nПостроить график (2): ",
    "UA": "Введеня прибутку (1)\nПобудувати графік (2): "
}

no_file_data_lang = {
    "EN": "There is no database file! Enter the data below",
    "RU": "Файл базы данных ещё не создан! Введите данные ниже для создания",
    "UA": "Файла бази даних ще не створено! Введіть дані нижче для створення файлу"
}

purchase_profit_mode_lang = {
    "EN": "Show profit (0), Show Purchases (1): ",
    "RU": "Просмотр прибыли (0), просмотр кол-ва продаж (1): ",
    "UA": "Дивитись прибуток (0), дивитись кількість продаж (1): "
}

overall_mode_profit_lang = {
    "EN": "Overall profit at period? Yes (1), No (0): ",
    "RU": "Общая прибыль за период? Да (1), Нет(0): ",
    "UA": "Загальний прибуток за період? Так (1), Ні (0): "
}

overall_mode_purchases_lang = {
    "EN": "Overall amount of purchases at period? Yes (1), No (0): ",
    "RU": "Общее количество продаж за период? Да (1), Нет (0): ",
    "UA": "Загальний кількість продаж за період? Так (1), Ні (0): "
}

incorrect_data_lang = {
    "EN": "Incorrect data entry!",
    "RU": "Некорректный ввод данных!",
    "UA": "Неправильне введення даних!" 
}

update_file_lang = {
    "EN": "Database file successfully updated with data above!",
    "RU": "Файл базы данных успешно обновлён с введёнными выше значениями!",
    "UA": "Файл бази даних успішно оновлений з вищевказаними значеннями!"    
}

create_file_lang = {
    "EN": "Database file file successfully created with data above! ",
    "RU": "Файл базы данных успешно создан с введёнными выше значениями! ",
    "UA": "Файл бази даних успішно створено з вищевказаними значеннями! "    
}

create_file_enter_lang = {
    "EN": ['day', 'cash profit', 'cashless profit', 'purchases'],
    "RU": ['день', 'прибыль наличными', 'прибыль безналичными', 'продажи'],
    "UA": ['день', 'прибуток готівкою', 'безготівковий прибуток', 'продажі']  
}

create_file_random_lang = {
    "EN": "Enter 'random' for generate random data: ",
    "RU": "Введите 'random' для генерации случайных данных: ",
    "UA": "Введіть 'random' для генерації довільних даних: "    
}

leave_empty_lang = {
    "EN": "Leave blank if the date is today!",
    "RU": "Оставьте пустым если дата текущая!",
    "UA": "Не пишіть нічого якщо дата поточна!"    
}

incorrect_day_lang = {
    "EN": "Incorrect day entry!\nEnter date in yyyy-mm-dd format!",
    "RU": "Некорректный ввод даты!\nВведите дату в формате гггг-мм-дд!",
    "UA": "Неправильне введення дати!\nВведіть дату у форматі рррр-мм-дд!"
}

answer_enter_lang = {
    "EN": "Enter",
    "RU": "Введите",
    "UA": "Введіть"    
}

does_not_exist_lang = {
    "EN": "\nTime period not found in database file!\nReturn to main menu...",
    "RU": "\nПериод не найден в базе данных!\nВозврат в главное меню...",
    "UA": "\nВказаний період не знайдено у базі даних!\nВихід у головне меню..."    
}

profit_label_lang = {
    "EN": "Profit, c.u.",
    "RU": "Доход, у.е.",
    "UA": "Прибуток, у.о."    
}

purchases_label_lang = {
    "EN": "Number of sales",
    "RU": "Количество продаж",
    "UA": "Кількість продажів"    
}

profit_title_lang = {
    "EN": "Profit in",
    "RU": "Доход за",
    "UA": "Прибуток за"    
}

purchases_title_lang = {
    "EN": "Number of sales by",
    "RU": "Количество продаж за",
    "UA": "Кількість продажів за"    
}

hover_annotation_day_lang = {
    "EN": "Day: ",
    "RU": "День",
    "UA": "День"    
}

hover_annotation_month_lang = {
    "EN": "Month:",
    "RU": "Месяц:",
    "UA": "Місяць:"    
}

hover_annotation_year_lang = {
    "EN": "Year:",
    "RU": "Год:",
    "UA": "Рік:"    
}

hover_annotation_value_lang = {
    "EN": "Value:",
    "RU": "Значение:",
    "UA": "Значення:"    
}

average_profit_lang = {
    "EN": "average profit (c.u.):",
    "RU": "средний доход (у.е.):",
    "UA": "середній прибуток у.о.):"
}

average_purchases_lang = {
    "EN": "average amount:",
    "RU": "среднее кол-во:",
    "UA": "середня кількість:"
}

enter_quit_add_data_lang = {
    "EN": "Enter 'q' to exit add data mode at any time!",
    "RU": "Введите 'q' в любой момент для выхода из режима добавления!",
    "UA": "Введіть 'q' для виходу з режиму додавання в будь-який момент!"    
}

quit_add_data_lang = {
    "EN": "Back to main menu? Leave blank empty if No, else (1) - Yes: ",
    "RU": "Вернуться в главное меню? Оставьте поле пустым если нет, если да - введите что угодно: ",
    "UA": "Повернутись у головне меню? Залиште поле пустим якщо ні, інакше введіть що завгодно: "
}

date_already_in_DB = {
    "EN": "This date is already in database! Period is not added...",
    "RU": "Дата уже есть в базе данных! Период не добавлен...",
    "UA": "Ці дані вже існують в базі Дданих! Період не додано..."
}

enter_years_lang = {
    "EN": "Enter periods in format (yyyy): ",
    "RU": "Введите периоды в формате (гггг): ",
    "UA": "Введіть періоди у форматі (рррр): "
}

enter_month_lang = {
    "EN": "Enter periods in format (yyyy-mm): ",
    "RU": "Введите периоды в формате (гггг-мм): ",
    "UA": "Введіть періоди у форматі (рррр-мм): "
}

max_value_lang = {
    "EN": "Max value is",
    "RU": "Наибольшее значение",
    "UA": "Максимальне значення"
}

min_value_lang = {
    "EN": "Min value is",
    "RU": "Наименьшее значение",
    "UA": "Мінімальне значення"
}

max_min_period_lang = {
    "EN": "by period",
    "RU": "за период",
    "UA": "за період"
}

random_year_lang = {
    "EN": "Enter how much years to generate: ",
    "RU": "Введите количество лет: ",
    "UA": "Введіть кількість років: "
}

randomize_msg_lang = {
    "EN": "This script generates random values to database, starts from 2020.\nWARNING!\nMaximum amount of years is unlimited!",
    "RU": "Этот скрипт создаст рандомные значения, начиная с 2020 года.\nВНИМАНИЕ!\nМаксимальное количество лет неограничено!",
    "UA": "Цей скрипт створює випадкові значення починаючи с 2020 року.\nУВАГА!\nМаксимальная кількість років необмежена!"    
}