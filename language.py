def choose_language():
    while True:
        lang = input('Choose a language\nВыберите язык\nОберіть мову\nEN/RU/UA: ')
        if lang.lower() == 'en' or len(lang) == 0:
            return "EN"
        elif lang.lower() == 'ru':
            return "RU"
        elif lang.lower() == 'ua':
            return "UA"
        else:
            print('Incorrect lang select!\nВведены неправилные данные!\nВведено неправильні дані!')

input_mode_lang = {
    "EN": "Enter data (1)\nBuild a graph (2): ",
    "RU": "Ввод прибыли (1)\nПостроить график (2): ",
    "UA": "Введеня прибутку (1)\nПобудувати графік (2): "
}

no_file_data_lang = {
    "EN": "There is no 'data.json' file! Enter the data below",
    "RU": "Файл data.json не создан! Введите данные ниже для создания",
    "UA": "Файла data.json не створено! Введіть дані нижче для створення файлу"
}

purchase_profit_mode_lang = {
    "EN": "Show profit (0), Show Purchases (1): ",
    "RU": "Просмотр прибыли (0), просмотр кол-ва продаж (1): ",
    "UA": "Дивитись прибуток (0), дивитись кількість продаж (1): "
}

compare_mode_lang = {
    "EN": "Compare two periods? Yes (1), No (0): ",
    "RU": "Сравнить два периода? Да (1), Нет (0): ",
    "UA": "Порівняти два періода? Так (1), Ні (0): "
}

overall_mode_profit_lang = {
    "EN": "Overall profit at period? Yes (1), No (0): ",
    "RU": "Общая прибыль за период? Да (1), Нет(0): ",
    "UA": "Загальний прибуток за період? Так (1), Ні (0): "
}

overall_mode_purchases_lang = {
    "EN": "Overall amount of purchases at period? Yes (1), No (0): ",
    "RU": "Общее количество продаж за период? Да (1), Нет(0): ",
    "UA": "Загальний кількість продаж за період? Так (1), Ні (0): "
}

per_start_lang = {
    "EN": "Enter first period (YYYY-MM): ",
    "RU": "Введите первый период (YYYY-MM): ",
    "UA": "Введіть перший період (YYYY-MM): "
}

per_end_lang = {
    "EN": "Enter second period (YYYY-MM): ",
    "RU": "Введите второй период (YYYY-MM): ",
    "UA": "Введіть другий період (YYYY-MM): "    
}

one_per_lang = {
    "EN": "Enter period (YYYY-MM): ",
    "RU": "Введите период (YYYY-MM): ",
    "UA": "Введіть період (YYYY-MM): "     
}

incorrect_data_lang = {
    "EN": "Incorrect data entry! ",
    "RU": "Некорректный ввод данных! ",
    "UA": "Неправильне введення даних! " 
}

update_file_lang = {
    "EN": "data.json file successfully updated with data above! ",
    "RU": "Файл data.json успешно обновлён с введёнными выше значениями! ",
    "UA": "Файл data.json успішно оновлений з вищевказаними значеннями! "    
}

create_file_lang = {
    "EN": "data.json file successfully created with data above! ",
    "RU": "Файл data.json успешно создан с введёнными выше значениями! ",
    "UA": "Файл data.json успішно створено з вищевказаними значеннями! "    
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
    "EN": "Incorrect day entry!\nEnter date in yyyy-mm format!",
    "RU": "Некорректный ввод даты!\nВведите дату в формате yyyy-mm!",
    "UA": "Неправильне введення дати!\nВведіть дату у форматі yyyy-mm!"    
}

answer_enter_lang = {
    "EN": "Enter",
    "RU": "Введите",
    "UA": "Введіть"    
}

back_to_main_menu_lang = {
    "EN": "Back to main menu? Yes (1), No (0)",
    "RU": "Вернуться в главное меню? Да (1), Нет (0)",
    "UA": "Повернутись у головне меню? Так (1), Ні (0)"    
}

does_not_exist_lang = {
    "EN": "\nTime period not found in data.json!\nReturn to main menu...",
    "RU": "\nПериод не найден в data.json!\nВозврат в главное меню...",
    "UA": "\nВказаний період не знайдено у data.json!\nВихід у головне меню..."    
}

profit_label_lang = {
    "EN": "Profit, c.u.",
    "RU": "Доход, у.е.",
    "UA": "Прибуток, у.о."    
}

purchases_label_lang = {
    "EN": "Amount of purchases",
    "RU": "Количество продаж",
    "UA": "Кількість продажів"    
}

profit_title_lang = {
    "EN": "Profit amount in",
    "RU": "Доход за",
    "UA": "Прибуток за"    
}

purchases_title_lang = {
    "EN": "Amount of purchases in",
    "RU": "Количество продаж за",
    "UA": "Кількість продажів за"    
}

hover_annotation_day_lang = {
    "EN": "Date",
    "RU": "Дата",
    "UA": "Дата"    
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
