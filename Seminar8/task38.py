import os

def show_menu():
    '''Функция меню
    '''
    os.system('clear')
    print("\nВыберите необходимое действие:\n"
          "1. Вывести справочник на экран\n"
          "2. Сохранить справочник в текстовом файле\n"
          "3. Найти абонента по фамилии\n"
          "4. Найти абонента по имени\n"
          "5. Добавить абонента в текстовый файл\n"
          "6. Изменить данные абонента\n"
          "7. Удалить абонента из текстового файла\n"
          "8. Завершить работу программы\n")
    choice = input('> ')
    if choice.isdigit(): return int(choice)
    return show_menu()

def go_to_function(variant):
    '''Функция адресации выполнения задач
    '''
    while (variant != 8):
        if variant == 1:
            for line in read_from_txt(filename):
                print(*line, end='')
            pause()
        elif variant == 2:
            write_to_txt(filename, abon_list)
            print('\nфайл сохранён !', end='')
            pause()
        elif variant == 3:
            finder = input_finder('введите фамилию абонента')
            find_abonent(filename, finder)
            pause()              
        elif variant == 4:
            finder = input_finder('введите имя абонента')
            find_abonent(filename, finder)
            pause()
        elif variant == 5:
            add_to_txt(filename)
            print('\nданные внесены !', end='')
            pause()
        elif variant == 6:
            for line in read_from_txt(filename):
                print(*line, end='')
            finder = input_finder('\n\nданные какого абонента вы ходите изменить?\nВведите его фамилию')
            redact_txt(filename, finder)
            pause()
        elif variant == 7:
            finder = input_finder('введите фамилию или имя абонента')
            del_from_txt(filename, finder)
            print('\nданные удалены !', end='')
            pause()
        variant = show_menu()

def read_from_txt(filename):
    '''Функция импорта списка из txt файла
    '''
    phone_list = [fields]
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            phone_list.append(line.split(','))
    return phone_list

def write_to_txt(filename, phone_dict):
    '''Функция экспорта списка abon_list в txt файл
    '''
    with open(filename, 'w', encoding='utf-8') as file:
        for line in phone_dict:
            file.write(",".join(line))

def add_to_txt(filename, line = []):
    '''Функция добавления записей в txt файл
    '''
    print('введите следующие данные для записи в справочник:')
    for item in fields:
        line.append(input(f'\n{item.strip()} > ').title())
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(f'{",".join(line)}\n')

def del_from_txt(filename, find_param):
    '''Функция удаления записи абонента из txt файла
    '''
    phone_book = read_from_txt(filename)[1:]
    for line in phone_book:
        if find_param in line:
            print(*line)
            phone_book.remove(line)
    write_to_txt(filename, phone_book)

def redact_txt(filename, find_param):
    '''Функция замены данных абонента в txt файле
    '''
    list_word = ['фамилию', 'имя', 'отчество', 'номер телефона']
    print('какие старые данные необходимо изменить:')
    for word in list_word:
        print(f'{list_word.index(word) + 1} - {word}')
    ind = (input('введите соответствующее число > '))
    if ind.isdigit():
        ind = int(ind)
        if 1 <= ind <= 4:
            new_data = input(f'Теперь новое значение - введите {list_word[ind-1]} > ').title()
            flag = False # Проверка наличия искомого абонента
            phone_book = read_from_txt(filename)[1:]
            for line in phone_book:
                if find_param in line:
                    flag = True
                    line[ind-1] = new_data
                    print(*line)
            if flag:
                write_to_txt(filename, phone_book)
                print('\nизменения внесены !', end='')
                return
    print("Вы ввели неверное значение!", end='')

def input_finder(message):
    '''Функция запроса данных от пользователя
    '''
    answer = input(f'\n{message} > ').title()
    print('\n')
    return answer

def pause():
    '''Функция ожидания нажатия клавиши пользователем
    '''
    input('\nнажмите Enter для продолжения...')

def find_abonent(filename, find_param):
    '''Функция поиска строки данных по запросу пользователя
    '''
    phone_list = read_from_txt(filename)
    find_list = []
    for line in phone_list:
        if find_param in line:
            find_list.append(line)
    if len(find_list) == 0: print('нет данных!')
    else: 
        find_list.insert(0, fields)
        for line in find_list:
            print(*line, end='')
        return find_list


filename = './Seminar8/phone.txt'
fields = ["Фамилия", "Имя", "Отчество", "Телефон\n\n"]
abon_list = [
    ['Пушкин','Александр','Сергеевич','999\n'],
    ['Есенин','Сергей','Александрович','123\n'],
    ['Булгаков','Михаил','Афанасьевич','987\n']
]
go_to_function(show_menu())