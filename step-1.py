import os
import shutil
import platform
import random


# Функции файлового менеджера

def create_folder():
    folder_name = input("Введите название папки: ")
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Папка {folder_name} создана.")
    else:
        print(f"Папка {folder_name} уже существует.")


def delete_item():
    item_name = input("Введите название файла или папки для удаления: ")
    if os.path.exists(item_name):
        if os.path.isdir(item_name):
            shutil.rmtree(item_name)
        else:
            os.remove(item_name)
        print(f"Элемент {item_name} удален.")
    else:
        print(f"Элемент {item_name} не найден.")


def copy_item():
    item_name = input("Введите название файла или папки для копирования: ")
    new_name = input("Введите новое название файла или папки: ")
    if os.path.exists(item_name):
        if os.path.isdir(item_name):
            shutil.copytree(item_name, new_name)
        else:
            shutil.copy(item_name, new_name)
        print(f"Элемент {item_name} скопирован как {new_name}.")
    else:
        print(f"Элемент {item_name} не найден.")


def list_directory_contents():
    for item in os.listdir():
        print(item)


def list_folders():
    for item in os.listdir():
        if os.path.isdir(item):
            print(item)


def list_files():
    for item in os.listdir():
        if os.path.isfile(item):
            print(item)


def os_info():
    print(platform.platform())


def creator_info():
    print("Программа создана Светланой Флегонтовой.")


def change_directory():
    new_path = input("Введите путь к новой рабочей директории: ")
    try:
        os.chdir(new_path)
        print(f"Рабочая директория изменена на {new_path}.")
    except FileNotFoundError:
        print("Указанный путь не найден.")
    except NotADirectoryError:
        print("Указанный путь не является директорией.")
    except PermissionError:
        print("Недостаточно прав для доступа к указанной директории.")


# Функция для викторины

def play_quiz():
    people = {
        'В.И Ленин': '22.04.1870',
        'Марк Твен': '30.11.1835',
        'Исаак Ньютон': '04.01.1643',
        'Людвиг VI': '01.01.1328',
        'Рюрик': '01.01.830',
        'Альберт Эйнштейн': '14.03.1879',
        'Наполеон Бонапарт': '15.08.1769',
        'Уильям Шекспир': '26.04.1564',
        'Галилео Галилей': '15.02.1564',
        'Джордж Вашингтон': '22.02.1732'
    }

    people_list = list(people.items())

    def format_birth_date(birth_date):
        day, month, year = birth_date.split('.')
        months = {
            '01': 'января', '02': 'февраля', '03': 'марта',
            '04': 'апреля', '05': 'мая', '06': 'июня',
            '07': 'июля', '08': 'августа', '09': 'сентября',
            '10': 'октября', '11': 'ноября', '12': 'декабря'
        }
        return f"{int(day)} {months[month]} {year} года"

    while True:
        random_people = random.sample(people_list, 5)
        selected_names = [person[0] for person in random_people]
        selected_birth_dates = [person[1] for person in random_people]

        correct_count = 0
        total_questions = len(selected_names)

        print("Отгадайте даты рождения для следующих известных людей:")

        for i in range(total_questions):
            name = selected_names[i]
            correct_birth_date = selected_birth_dates[i]

            print(f"{i + 1}. В каком году родился {name}? (введите в формате dd.mm.yyyy): ")
            user_input = input()

            if user_input == correct_birth_date:
                print("Правильно!")
                correct_count += 1
            else:
                print(f"Неправильно. Правильный ответ: {format_birth_date(correct_birth_date)}")

        print(f'\nКоличество правильных ответов: {correct_count}')
        print(f'Количество неправильных ответов: {total_questions - correct_count}')
        print(f'Процент правильных ответов: {correct_count * (100 / total_questions)}%')
        print(f'Процент неправильных ответов: {(total_questions - correct_count) * (100 / total_questions)}%')

        play_again = input('\nХотите начать игру заново? (Да/нет): ').strip().lower()
        if play_again != 'да' and play_again != 'yes':
            break


# Функция для управления банковским счетом

def bank_account():
    balance = 0
    purchases = []

    def add_funds(amount):
        nonlocal balance
        balance += amount

    def make_purchase(amount, item):
        nonlocal balance
        balance -= amount
        purchases.append((item, amount))

    def show_purchase_history():
        if not purchases:
            print("История покупок пуста.")
        else:
            for item, amount in purchases:
                print(f"Покупка: {item}, Сумма: {amount}")

    while True:
        print("\n1. пополнение счета")
        print("2. покупка")
        print("3. история покупок")
        print("4. выход")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            try:
                amount = float(input("Введите сумму для пополнения счета: "))
                add_funds(amount)
                print(f"Счет пополнен на {amount}. Текущий баланс: {balance}.")
            except ValueError:
                print("Пожалуйста, введите корректную сумму.")
        elif choice == '2':
            try:
                amount = float(input("Введите сумму покупки: "))
                if amount > balance:
                    print("Недостаточно средств на счете.")
                else:
                    item = input("Введите название покупки: ")
                    make_purchase(amount, item)
                    print(f"Покупка {item} на сумму {amount} успешно выполнена. Текущий баланс: {balance}.")
            except ValueError:
                print("Пожалуйста, введите корректную сумму.")
        elif choice == '3':
            show_purchase_history()
        elif choice == '4':
            print("Выход из программы.")
            break
        else:
            print("Неверный пункт меню. Пожалуйста, выберите снова.")


# Основная функция

def main():
    while True:
        print("\nМеню:")
        print("1. Создать папку")
        print("2. Удалить (файл/папку)")
        print("3. Копировать (файл/папку)")
        print("4. Просмотр содержимого рабочей директории")
        print("5. Посмотреть только папки")
        print("6. Посмотреть только файлы")
        print("7. Просмотр информации об операционной системе")
        print("8. Создатель программы")
        print("9. Играть в викторину")
        print("10. Мой банковский счет")
        print("11. Смена рабочей директории")
        print("12. Выход")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            create_folder()
        elif choice == '2':
            delete_item()
        elif choice == '3':
            copy_item()
        elif choice == '4':
            list_directory_contents()
        elif choice == '5':
            list_folders()
        elif choice == '6':
            list_files()
        elif choice == '7':
            os_info()
        elif choice == '8':
            creator_info()
        elif choice == '9':
            play_quiz()
        elif choice == '10':
            bank_account()
        elif choice == '11':
            change_directory()
        elif choice == '12':
            print("Выход из программы.")
            break
        else:
            print("Неверный пункт меню. Пожалуйста, выберите снова.")


if __name__ == "__main__":
    main()
