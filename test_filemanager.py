import os
import shutil
import pytest
from unittest.mock import patch
from io import StringIO
from file_manager import create_folder, delete_item, copy_item, list_directory_contents, \
    list_folders, list_files, os_info, creator_info, change_directory, \
    play_quiz, bank_account, save_account_data, load_account_data, \
    save_directory_contents, load_directory_contents


@pytest.fixture
def setup_test_directory():
    test_dir = 'test_dir'
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
    test_file = os.path.join(test_dir, 'test_file.txt')
    with open(test_file, 'w') as f:
        f.write('Test content')
    yield test_dir
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)


@patch('builtins.input', return_value='test_folder')
@patch('builtins.print')
def test_create_folder(mock_print, mock_input):
    create_folder()
    assert os.path.exists('test_folder')
    shutil.rmtree('test_folder')


@patch('builtins.input', return_value='nonexistent_item')
@patch('builtins.print')
def test_delete_nonexistent_item(mock_print, mock_input):
    delete_item()
    mock_print.assert_called_with('Элемент nonexistent_item не найден.')


@patch('builtins.input', side_effect=['test_file.txt', 'test_file_copy.txt'])
@patch('builtins.print')
def test_copy_item(mock_print, mock_input, setup_test_directory):
    os.chdir(setup_test_directory)
    copy_item()
    assert os.path.exists('test_file_copy.txt')


def test_list_directory_contents(setup_test_directory):
    with patch('sys.stdout', new_callable=lambda: StringIO()) as fake_out:
        os.chdir(setup_test_directory)
        list_directory_contents()
        output = fake_out.getvalue().strip()
        assert 'test_file.txt' in output


def test_list_folders(setup_test_directory):
    with patch('sys.stdout', new_callable=lambda: StringIO()) as fake_out:
        os.makedirs(os.path.join(setup_test_directory, 'test_folder'))
        os.chdir(setup_test_directory)
        list_folders()
        output = fake_out.getvalue().strip()
        assert 'test_folder' in output


def test_list_files(setup_test_directory):
    with patch('sys.stdout', new_callable=lambda: StringIO()) as fake_out:
        os.chdir(setup_test_directory)
        list_files()
        output = fake_out.getvalue().strip()
        assert 'test_file.txt' in output


@patch('builtins.print')
def test_os_info(mock_print):
    os_info()
    mock_print.assert_called()


@patch('builtins.print')
def test_creator_info(mock_print):
    creator_info()
    mock_print.assert_called_with('Программа создана Светланой Флегонтовой.')


@patch('builtins.input', return_value='nonexistent_directory')
@patch('builtins.print')
def test_change_directory_not_found(mock_print, mock_input):
    change_directory()
    mock_print.assert_called_with('Указанный путь не найден.')


@patch('builtins.input', return_value='14.03.1879')
@patch('builtins.print')
def test_play_quiz_correct_answer(mock_print, mock_input):
    with patch('random.sample', return_value=[('Альберт Эйнштейн', '14.03.1879')]):
        play_quiz()
        mock_print.assert_any_call("Правильно!")


@patch('builtins.input', side_effect=['1', '100', '4'])
@patch('builtins.print')
def test_bank_account_deposit(mock_print, mock_input):
    bank_account()
    mock_print.assert_any_call("Счет пополнен на 100.0. Текущий баланс: 100.0.")


# Удалили тест `test_bank_account_purchase`, так как он больше не нужен

@patch('builtins.input', side_effect=['1', '100', '2', '50', 'Item', '4'])
@patch('builtins.print')
def test_bank_account_purchase(mock_print, mock_input):
    # Устанавливаем начальный баланс
    initial_balance = 100.0
    purchase_amount = 50.0
    expected_balance = initial_balance - purchase_amount
    expected_message = f"Покупка Item на сумму {purchase_amount} успешно выполнена. Текущий баланс: {expected_balance}."

    # Устанавливаем начальный баланс
    save_account_data(initial_balance, [], filename="test_account_data.json")

    # Запускаем функцию
    bank_account()

    # Получаем все вызовы print
    print_calls = [call[0][0] for call in mock_print.call_args_list]

    # Проверяем наличие ожидаемого сообщения
    assert expected_message in print_calls, f"Expected message not found. Calls: {print_calls}"


@patch('builtins.input', side_effect=['1', '100', '4'])
@patch('builtins.print')
def test_save_and_load_account_data(mock_print, mock_input):
    balance = 100.0
    purchases = [("item1", 50.0), ("item2", 25.0)]
    save_account_data(balance, purchases, filename="test_account_data.json")

    loaded_balance, loaded_purchases = load_account_data(filename="test_account_data.json")
    assert balance == loaded_balance
    assert [list(p) for p in purchases] == loaded_purchases


def test_save_directory_contents(setup_test_directory):
    with patch('builtins.print') as mock_print:
        os.chdir(setup_test_directory)
        save_directory_contents('listdir.txt')
        with open('listdir.txt', 'r') as f:
            content = f.read()
        assert 'test_file.txt' in content


def test_load_directory_contents(setup_test_directory):
    with open('listdir.txt', 'w') as f:
        f.write('test_file.txt')
    os.chdir(setup_test_directory)
    load_directory_contents('listdir.txt')
    assert os.path.exists('test_file.txt')
    os.remove('test_file.txt')
