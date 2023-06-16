import os
import sys

def Check(word) :
    if word == 'ok' or word == 'ок' :
        return True
    else :
        return False

def CheckNum(message) :
    try :
        num = input(message)
        if num == '' :
            return Main()
        else :
            num = int(num) - 1
            return num
    except ValueError :
        print('Неверное значениее, попробуйте ввести заново')
        return CheckNum()
    
def FilterWord1(letter) :
    if letter in '\/.,`1234567890-=+_)(*&^%$#@!~<>?":;№[]|}{' :
        return False
    elif letter in "'" :
        return False
    else :
        return True
    
def FilterWord (n) :
    return ''.join(str(item) for item in filter(FilterWord1, n))

def FilterNumber1(num) :
    if num in '\/.,`-=+_)(*&^%$#@!~<>?":;№[]|}{' :
        return False
    elif num in "qwertyuiopasdfghjklzxcvbnmёйцукенгшщзхъфывапролджэячсмитьбю'" :
        return False
    else :
        return True

def FilterNumber(num) :
    return ''.join(str(item) for item in filter(FilterNumber1, num))

def ShowContats(file_name) :
    os.system('CLS')
    with open(file_name, 'r', encoding='utf-8') as file :
        data = file.readlines()

        for contact in data :
            print(contact)
    input('Нажмите Enter или введите любой символ для возврата: ')
    return Main()

def AddContact(file_name) :
    os.system('CLS')
    with open(file_name, 'a', encoding='utf-8') as file :
        contact = ''
        surname = input('Введите Фамилию контакта: ').title()
        contact += FilterWord(surname) + ' '
        name = input('Введите Имя контакта: ').title()
        contact += FilterWord(name) + ' '
        number = input('Введите номер контакта: ').lower()
        contact += '+' + FilterNumber(number)


        file.write(contact)
        file.write('\n')
    print()
    ShowContats(file_name)
    print()

def Search(file_name) :
    os.system('CLS')
    target = input('Введите Фамилию и/или Имя для поиска: ').title()
    target = FilterWord(target)

    with open (file_name, 'r', encoding='utf-8' ) as file :
        contacts = file.readlines()

        for contact in contacts :
            if target in contact :
                print(contact)
    
    n = input('Введите "ОК" для продолжения или любой символ для возврата: ').lower
    if Check(n) :
        return Search(file_name)

def Change(file_name) :
    os.system('CLS')
    with open (file_name, 'r', encoding='utf-8') as file :
        contacts = file.readlines()
        change = []
        for contact in contacts :
            change.append(contact)
        
        for i in range(len(change)) :
            print(i+1, change[i])
        n = CheckNum('Введите номер контакта, который хотите изменить или enter, если хотите вернуться в меню: ')
        try :
            contact = list(str(change[n]).split())
        except IndexError :
            input('Контакта под таким номером нет! Попробуйте снова!')
            return Change(file_name)
        os.system('CLS')
    with open (file_name, 'w+', encoding='utf-8') as file :
        print('1 - Фамилию')
        print('2 - Имя')
        print('3 - Номер')
        
        c = CheckNum('Укажите, что хотите изменить: ') - 1
        if c == 0 :
            contact[c] = input('Введите новую Фамилию: ').title()
            contact[c] = FilterWord(contact[c])
        elif c == 1 :
            contact[c] = input('Введите новое Имя: ').title()
            contact[c] = FilterWord(contact[c])
        elif c == 2 :
            contact[c] = input('Введите новый номер: ').lower()
            contact[c] = FilterNumber(contact[c])
        else :
            print('Введено неверное значение!')

        contact = ' '.join(str(item) for item in contact)
        change[n] = contact
        for i in range(len(change)) :
            print(i+1, change[i])
            file.write(change[i])
        
    n = input('Введите "ОК" для продолжения или любой символ для возврата: ').lower()
    if Check(n) :
        return Change(file_name)
    else :
        return Main()

def Delete(file_name) :
    os.system('CLS')
    with open (file_name, 'r', encoding='utf-8') as file :
        contacts = file.readlines()
        change = []
        for contact in contacts :
            change.append(contact)
        
        for i in range(len(change)) :
            print(i+1, change[i])
        n = CheckNum('Введите номер контакта, который хотите удалить: ')

        try :   
            change.pop(n-1)
        except IndexError :
            input('Контакта под таким номером нет! Попробуйте снова!')
            return Delete(file_name)

        os.system('CLS')
    with open (file_name, 'w', encoding='utf-8') as file :
        for i in range(len(change)) :
            print(i+1, change[i])
            file.write(change[i])
    
    n = input('Введите "ОК" для продолжения или любой символ для возврата: ').lower
    if Check(n) :
        return Delete(file_name)

def Drowing() :
    print('1 - Показать контакты')
    print('2 - Добавить контакт')
    print('3 - Изменить контакт')
    print('4 - Удалить контакт')
    print('5 - Поиск контакта')
    print('6 - Выход')

def Choice(user_choice) :
    if user_choice == 1 :
        ShowContats('PhoneBook.txt')
    elif user_choice == 2 :
        AddContact('PhoneBook.txt')
    elif user_choice == 3 :
        Change('PhoneBook.txt')
    elif user_choice == 4 :
        Delete('PhoneBook.txt')
    elif user_choice == 5 :
        Search('PhoneBook.txt')
    elif user_choice == 6 :
        print('Программа завершена!')
        sys.exit()

def Main() :
    while True :
        os.system('CLS')
        Drowing()
        try :
            user_choice = int(input('Введите цифру от 1 до 6: '))
        except ValueError :
            print('Неверное значение!')
            input('Нажмите любую кнопку для возврата')
            return Main()
        Choice(user_choice)

Main()