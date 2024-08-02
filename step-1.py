from file_manager import create_folder, delete_item, copy_item, list_directory_contents, \
                         list_folders, list_files, os_info, creator_info, change_directory, \
                         play_quiz, bank_account, save_directory_contents

def main_menu():
    while True:
        print("\n1. создать папку")
        print("2. удалить файл/папку")
        print("3. копировать файл/папку")
        print("4. просмотр содержимого рабочей директории")
        print("5. показать только папки")
        print("6. показать только файлы")
        print("7. информация о системе")
        print("8. создатель программы")
        print("9. смена рабочей директории")
        print("10. угадать число")
        print("11. мой банковский счет")
        print("12. сохранить содержимое рабочей директории в файл")
        print("0. выход")

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
            change_directory()
        elif choice == '10':
            play_quiz()
        elif choice == '11':
            bank_account()
        elif choice == '12':
            save_directory_contents()
        elif choice == '0':
            print("Выход из программы.")
            break
        else:
            print("Неверный пункт меню. Пожалуйста, выберите снова.")

if __name__ == "__main__":
    main_menu()
