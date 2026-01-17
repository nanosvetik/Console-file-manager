import os
import shutil
import platform
import random
import json
from functools import wraps


def handle_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An error occurred: {e}")
    return wrapper


def load_account_data(filename="account_data.json"):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return data.get("balance", 0), data.get("purchases", [])
    except FileNotFoundError:
        return 0, []


def save_account_data(balance, purchases, filename="account_data.json"):
    data = {
        "balance": balance,
        "purchases": purchases
    }
    with open(filename, "w") as file:
        json.dump(data, file)


@handle_exceptions
def create_folder():
    folder_name = input("Введите название папки: ")
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Папка {folder_name} создана.")
    else:
        print(f"Папка {folder_name} уже существует.")


@handle_exceptions
def delete_item():
    item_name = input("Введите название файла или папки для удаления: ")
    if os.path.exists(item_name):
        shutil.rmtree(item_name) if os.path.isdir(item_name) else os.remove(item_name)
        print(f"Элемент {item_name} удален.")
    else:
        print(f"Элемент {item_name} не найден.")


@handle_exceptions
def copy_item():
    item_name = input("Введите название файла или папки для копирования: ")
    new_name = input("Введите новое название файла или папки: ")
    if os.path.exists(item_name):
        shutil.copytree(item_name, new_name) if os.path.isdir(item_name) else shutil.copy(item_name, new_name)
        print(f"Элемент {item_name} скопирован как {new_name}.")
    else:
        print(f"Элемент {item_name} не найден.")


@handle_exceptions
def save_directory_contents(filename="listdir.txt"):
    files = (item for item in os.listdir() if os.path.isfile(item))
    dirs = (item for item in os.listdir() if os.path.isdir(item))

    with open(filename, "w") as file:
        file.write("files: " + ", ".join(files) + "\n")
        file.write("dirs: " + ", ".join(dirs) + "\n")
    print(f"Содержимое текущей директории сохранено в {filename}.")


def show_system_info():
    print(f"Операционная система: {platform.system()}")
    print(f"Имя компьютера: {platform.node()}")
    print(f"Процессор: {platform.processor()}")


@handle_exceptions
def play_guessing_game():
    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Угадайте число от 1 до 100: "))
            attempts += 1
            if guess < number:
                print("Загаданное число больше.")
            elif guess > number:
                print("Загаданное число меньше.")
            else:
                print(f"Поздравляем! Вы угадали число {number} за {attempts} попыток.")
                break
        except ValueError:
            print("Пожалуйста, введите корректное число.")

    play_again = input("Хотите сыграть еще раз? (да/нет): ").strip().lower()
    if play_again in ('да', 'yes'):
        play_guessing_game()


def bank_account():
    balance, purchases = load_account_data()

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
            save_account_data(balance, purchases)
            print("Данные сохранены. Выход из программы.")
            break
        else:
            print("Неверный пункт меню. Пожалуйста, выберите снова.")


