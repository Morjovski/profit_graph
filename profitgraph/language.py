import colorama

colorama.init()

yellow = colorama.Fore.YELLOW
red = colorama.Fore.RED
green = colorama.Fore.GREEN
color_reset = colorama.Fore.RESET


def choose_language() -> str:
    while True:
        lang = input(f'\nChoose a language\nВыберите язык\nОберіть мову\n'
                     f'{yellow}EN{color_reset}/{yellow}RU{color_reset}/{yellow}UA{color_reset}: ')
        if lang.lower() == 'en' or len(lang) == 0:
            return "EN"
        elif lang.lower() == 'ru' or lang.lower() == 'кг':
            return "RU"
        elif lang.lower() == 'ua' or lang.lower() == 'гф':
            return "UA"
        else:
            print('\nIncorrect lang select!\nВведены неправилные данные!\nВведено неправильні дані!')


interval_mode_lang = {
    "EN": f"\nBuild graph by:\nYears at all - ({yellow}1{color_reset})\nYear by months - ({yellow}2{color_reset})\nMonths by days - ({yellow}3{color_reset})",
    "RU": f"\nПросмотр графика за:\nЗа года в общем - ({yellow}1{color_reset})\nЗа года помесячно - ({yellow}2{color_reset})\nЗа месяцы по дням - ({yellow}3{color_reset})",
    "UA": f"\nДивитись графік за:\nЗа роки в цілому - ({yellow}1{color_reset})\nЗа роки помісячно - ({yellow}2{color_reset})\nЗа місяці по днях - ({yellow}3{color_reset})"
}

interval_mode_input_lang = {
    "EN": "Enter interval mode: ",
    "RU": "Введите режим: ",
    "UA": "Введіть режим: "
}

input_mode_lang = {
    "EN": f"\nEnter data ({yellow}1{color_reset})\nBuild a graph ({yellow}2{color_reset}): ",
    "RU": f"\nВвод прибыли ({yellow}1{color_reset})\nПостроить график ({yellow}2{color_reset}): ",
    "UA": f"\nВведеня прибутку ({yellow}1{color_reset})\nПобудувати графік ({yellow}2{color_reset}): "
}

no_file_data_lang = {
    "EN": f"\nThere is {red}no database file{color_reset}! Enter the first data below",
    "RU": f"\nФайл базы данных ещё {red}не создан{color_reset}! Введите данные ниже для создания",
    "UA": f"\nФайла бази даних ще {red}не створено{color_reset}! Введіть дані нижче для створення файлу"
}

purchase_profit_mode_lang = {
    "EN": f"\nShow profit ({yellow}1{color_reset}), Show Purchases ({yellow}2{color_reset}): ",
    "RU": f"\nПросмотр прибыли ({yellow}1{color_reset}), просмотр кол-ва продаж ({yellow}2{color_reset}): ",
    "UA": f"\nДивитись прибуток ({yellow}1{color_reset}), дивитись кількість продаж ({yellow}2{color_reset}): "
}

overall_mode_profit_lang = {
    "EN": f"\nOverall profit at period? Yes ({yellow}1{color_reset}), No ({yellow}2{color_reset}): ",
    "RU": f"\nОбщая прибыль за период? Да ({yellow}1{color_reset}), Нет({yellow}2{color_reset}): ",
    "UA": f"\nЗагальний прибуток за період? Так ({yellow}1{color_reset}), Ні ({yellow}2{color_reset}): "
}

overall_mode_purchases_lang = {
    "EN": f"\nOverall amount of purchases at period? Yes ({yellow}1{color_reset}), No ({yellow}2{color_reset}): ",
    "RU": f"\nОбщее количество продаж за период? Да ({yellow}1{color_reset}), Нет ({yellow}2{color_reset}): ",
    "UA": f"\nЗагальний кількість продаж за період? Так ({yellow}1{color_reset}), Ні ({yellow}2{color_reset}): "
}

incorrect_data_lang = {
    "EN": f"\n{red}Incorrect data entry!{color_reset}",
    "RU": f"\n{red}Некорректный ввод данных!{color_reset}",
    "UA": f"\n{red}Неправильне введення даних!{color_reset}"
}

update_file_lang = {
    "EN": f"\nDatabase file {green}successfully updated{color_reset} with data above!",
    "RU": f"\nФайл базы данных {green}успешно обновлён{color_reset} с введёнными выше значениями!",
    "UA": f"\nФайл бази даних {green}успішно оновлено{color_reset} з вищевказаними значеннями!"    
}

create_file_lang = {
    "EN": f"\nDatabase file {green}successfully created{color_reset} with data above! ",
    "RU": f"\nФайл базы данных {green}успешно создан{color_reset} с введёнными выше значениями! ",
    "UA": f"\nФайл бази даних {green}успішно створено{color_reset} з вищевказаними значеннями! "    
}

success_db_delete_lang = {
    "EN": f"\nDatabase file {green}successfully deleted{color_reset}! ",
    "RU": f"\nФайл базы данных {green}успешно удалён{color_reset}! ",
    "UA": f"\nФайл бази даних {green}успішно видалено{color_reset}! "    
}

create_file_enter_lang = {
    "EN": [f'{yellow}day{color_reset}', f'{yellow}cash profit{color_reset}', f'{yellow}cashless profit{color_reset}', f'{yellow}purchases{color_reset}'],
    "RU": [f'{yellow}день{color_reset}', f'{yellow}прибыль наличными{color_reset}', f'{yellow}прибыль безналичными{color_reset}', f'{yellow}продажи{color_reset}'],
    "UA": [f'{yellow}день{color_reset}', f'{yellow}прибуток готівкою{color_reset}', f'{yellow}безготівковий прибуток{color_reset}', f'{yellow}продажі{color_reset}']  
}

day_format_lang = {
    "EN": f"in ({yellow}dd-mm-yyyy{color_reset}) format: ",
    "RU": f"в формате ({yellow}дд-мм-гггг{color_reset}): ",
    "UA": f"у форматі ({yellow}дд-мм-рррр{color_reset}: "
}

correct_day_format_lang = {
    "EN": f"You need to enter day in a ({yellow}yyyy-mm-dd{color_reset}) format!",
    "RU": f"Необходимо ввести дату в формате ({yellow}гггг-мм-дд{color_reset})!",
    "UA": f"Потрібно ввести день у форматі ({yellow}рррр-мм-дд{color_reset})!"
}

auto_day_enter_lang = {
    "EN": "The selected date is",
    "RU": "Выбранная дата -",
    "UA": "Обрана дата -"
}

create_file_random_lang = {
    "EN": f"\nEnter '{yellow}random{color_reset}' for generate random data: ",
    "RU": f"\nВведите '{yellow}random{color_reset}' для генерации случайных данных: ",
    "UA": f"\nВведіть '{yellow}random{color_reset}' для генерації довільних даних: "    
}

leave_empty_lang = {
    "EN": f"{yellow}Leave blank empty{color_reset} if the date is today!",
    "RU": f"{yellow}Оставьте пустым{color_reset} если дата текущая!",
    "UA": f"{yellow}Не пишіть нічого{color_reset} якщо дата поточна!"    
}

incorrect_day_lang = {
    "EN": f"\n{red}Incorrect day entry!{color_reset}\nEnter date in {yellow}yyyy-mm-dd{color_reset} format!\n",
    "RU": f"\n{red}Некорректный ввод даты!{color_reset}\nВведите дату в формате {yellow}гггг-мм-дд{color_reset}!\n",
    "UA": f"\n{red}Неправильне введення дати!{color_reset}\nВведіть дату у форматі {yellow}рррр-мм-дд{color_reset}!\n"
}

answer_enter_lang = {
    "EN": "Enter",
    "RU": "Введите",
    "UA": "Введіть"    
}

profit_label_lang = {
    "EN": "Profit (c.u.)",
    "RU": "Доход (у.е.)",
    "UA": "Прибуток (грн)"    
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

annotation_day_lang = {
    "EN": "Day",
    "RU": "День",
    "UA": "День"    
}

annotation_month_lang = {
    "EN": "Month",
    "RU": "Месяц",
    "UA": "Місяць"    
}

annotation_year_lang = {
    "EN": "Year",
    "RU": "Год",
    "UA": "Рік"    
}

hover_annotation_day_lang = {
    "EN": "Day:",
    "RU": "День:",
    "UA": "День:"    
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
    "EN": "average:",
    "RU": "среднее значение:",
    "UA": "середня кількість:"
}

compare_to_first_period_lang = {
    "EN": "compare to first period",
    "RU": "в сравнении с первым периодом",
    "UA": "у порівнянні з першим періодом"
}

enter_quit_add_data_lang = {
    "EN": f"\nEnter '{yellow}q{color_reset}' to exit add data mode at any time!",
    "RU": f"\nВведите '{yellow}q{color_reset}' в любой момент для выхода из режима добавления!",
    "UA": f"\nВведіть '{yellow}q{color_reset}' для виходу з режиму додавання в будь-який момент!"    
}

back_main_menu_lang = {
    "EN": f"\nEnter '{yellow}q{color_reset}' to go back to main menu at any time!",
    "RU": f"\nВведите '{yellow}q{color_reset}' в любой момент для выхода главное меню!",
    "UA": f"\nВведіть '{yellow}q{color_reset}' для виходу у головне меню в будь-який момент!"
}

quit_program_lang = {
    "EN": f"\nEnter '{yellow}quit{color_reset}' to shutdown the program!",
    "RU": f"\nВведите '{yellow}quit{color_reset}' для закрытия программы!",
    "UA": f"\nВведіть '{yellow}quit{color_reset}' для виходу з програми!"
}

quit_add_data_lang = {
    "EN": f"\nBack to main menu? Leave blank {yellow}empty{color_reset} if No, else entry {yellow}everything{color_reset}: ",
    "RU": f"\nВернуться в главное меню? Оставьте поле {yellow}пустым{color_reset} если нет, если да - введите {yellow}что угодно{color_reset}: ",
    "UA": f"\nПовернутись у головне меню? Залиште поле {yellow}пустим{color_reset} якщо ні, інакше введіть {yellow}що завгодно{color_reset}: "
}

date_already_in_DB = {
    "EN": f"\n{red}This date is already in database!{color_reset}\nPeriod is not added...",
    "RU": f"\n{red}Дата уже есть в базе данных!{color_reset}\nПериод не добавлен...",
    "UA": f"\n{red}Ці дані вже існують в базі Даних!{color_reset}\nПеріод не додано..."
}

enter_years_lang = {
    "EN": f"\nEnter periods in format ({yellow}yyyy{color_reset}) separated by a space: ",
    "RU": f"\nВведите периоды в формате ({yellow}гггг{color_reset}) через пробел: ",
    "UA": f"\nВведіть періоди у форматі ({yellow}рррр{color_reset}) через пропуск: "
}

enter_month_lang = {
    "EN": f"\nEnter periods in format ({yellow}yyyy-mm{color_reset}) separated by a space: ",
    "RU": f"\nВведите периоды в формате ({yellow}гггг-мм{color_reset}) через пробел: ",
    "UA": f"\nВведіть періоди у форматі ({yellow}рррр-мм{color_reset}) через пропуск: "
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
    "EN": "\nEnter how much years to generate: ",
    "RU": "\nВведите количество лет: ",
    "UA": "\nВведіть кількість років: "
}

randomize_msg_lang = {
    "EN": f"\nThis script generates random values to database, starts from {yellow}2020{color_reset}.\n{red}WARNING!{color_reset}\nMaximum amount of years is unlimited!",
    "RU": f"\nЭтот скрипт создаст рандомные значения, начиная с {yellow}2020{color_reset} года.\n{red}ВНИМАНИЕ!{color_reset}\nМаксимальное количество лет неограничено!",
    "UA": f"\nЦей скрипт створює випадкові значення починаючи с {yellow}2020{color_reset} року.\n{red}УВАГА!{color_reset}\nМаксимальная кількість років необмежена!"    
}

success_add_data_lang = {
    "EN": f"\nThe day has been {green}successfully added{color_reset}!",
    "RU": f"\nДень {green}успешно добавлен{color_reset} в базу данных!",
    "UA": f"\nДень {green}успішно додано{color_reset} до бази даних!"
}

select_language_lang = {
    "EN": f"\n{green}English has been selected.{color_reset}",
    "RU": f"\n{green}Выбран русский язык.{color_reset}",
    "UA": f"\n{green}Обрана українська мова.{color_reset}"
}

float_value_lang = {
    "EN": f"You need to enter a {yellow}real{color_reset} number or {yellow}natural{color_reset} number!",
    "RU": f"Нужно ввести {yellow}вещественное{color_reset} или {yellow}натуральное{color_reset} число!",
    "UA": f"Потрібно ввести {yellow}дійсне{color_reset} чи {yellow}натуральне{color_reset} число!"
}

int_value_lang = {
    "EN": f"You need to enter a {yellow}natural{color_reset} number!",
    "RU": f"Нужно ввести {yellow}целое{color_reset} число!",
    "UA": f"Потрібно ввести {yellow}ціле{color_reset} число!"
}

purchases_img_save_lang = {
    "EN": f"is {green}successfully saved{color_reset} into '{yellow}graphs/purchases{color_reset}' folder!",
    "RU": f"{green}успешно сохранён{color_reset} в папку '{yellow}graphs/purchases{color_reset}'!",
    "UA": f"{green}успішно збережено{color_reset} у папку '{yellow}graphs/purchases{color_reset}'!"
}

profit_img_save_lang = {
    "EN": f"is {green}successfully saved{color_reset} in folder:",
    "RU": f"{green}успешно сохранён{color_reset} в папку:",
    "UA": f"{green}успішно збережено{color_reset} у папку:"
}

success_random_data_lang = {
    "EN": f"\nRandom data is {green}successfully{color_reset} created in database!\n",
    "RU": f"\nСлучайные данные {green}успешно{color_reset} добавлены в базу данных!\n",
    "UA": f"\nВипадкові дані {green}успішно{color_reset} додані у базу даних\n"
}

exit_program_lang = {
    "EN": "Shutting down...",
    "RU": "Программа закрывается...",
    "UA": "Програма зачиняється..."
}

incorrect_year_lang = {
    "EN": f"\n{red}Incorrect periods format!{color_reset} Enter dates in format ({yellow}yyyy{color_reset}) separated by space!",
    "RU": f"\n{red}Неправильно введенные периоды!{color_reset} Введите даты в формате ({yellow}гггг{color_reset}), которые разделенные пробелом!",
    "UA": f"\n{red}Невірно введені періоди!{color_reset} Введіть дати у форматі ({yellow}рррр{color_reset}), які розділені пробілом!"
}

incorrect_year_month_lang = {
    "EN": f"\n{red}Incorrect periods format!{color_reset} Enter dates in format ({yellow}yyyy-mm{color_reset}) separated by space!",
    "RU": f"\n{red}Неправильно введенные периоды!{color_reset} Введите даты в формате ({yellow}гггг-мм{color_reset}), которые разделены пробелом!",
    "UA": f"\n{red}Невірно введені періоди!{color_reset} Введіть дати у форматі ({yellow}рррр-мм{color_reset}), які розділені пробілом!"
}

last_period_lang = {
    "EN": "\nLast added period is:",
    "RU": "\nПоследний добавленный период:",
    "UA": "\nОстанній доданий період:"
}

delete_db_lang = {
    "EN": f"Enter '{yellow}delete{color_reset}' to delete a database file!",
    "RU": f"Введите '{yellow}delete{color_reset}' для удаления файла базы данных!",
    "UA": f"Введіть '{yellow}delete{color_reset}' для видалення файла бази даних!"
}
