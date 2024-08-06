import unittest
from unittest.mock import patch, mock_open
import file_manager
import json
import os


class TestFileManager(unittest.TestCase):

    @patch("builtins.input", side_effect=["test_folder"])
    @patch("os.makedirs")
    @patch("os.path.exists", return_value=False)
    @patch("builtins.print")
    def test_create_folder(self, mock_print, mock_exists, mock_makedirs, mock_input):
        file_manager.create_folder()
        mock_makedirs.assert_called_with("test_folder")
        mock_print.assert_called_with("Папка test_folder создана.")

    @patch("builtins.input", side_effect=["test_folder"])
    @patch("os.path.exists", return_value=True)
    @patch("builtins.print")
    def test_create_folder_exists(self, mock_print, mock_exists, mock_input):
        file_manager.create_folder()
        mock_print.assert_called_with("Папка test_folder уже существует.")

    @patch("builtins.input", side_effect=["test_item"])
    @patch("os.path.exists", return_value=True)
    @patch("os.path.isdir", return_value=True)
    @patch("shutil.rmtree")
    @patch("builtins.print")
    def test_delete_item_folder(self, mock_print, mock_rmtree, mock_isdir, mock_exists, mock_input):
        file_manager.delete_item()
        mock_rmtree.assert_called_with("test_item")
        mock_print.assert_called_with("Элемент test_item удален.")

    @patch("builtins.input", side_effect=["test_item"])
    @patch("os.path.exists", return_value=True)
    @patch("os.path.isdir", return_value=False)
    @patch("os.remove")
    @patch("builtins.print")
    def test_delete_item_file(self, mock_print, mock_remove, mock_isdir, mock_exists, mock_input):
        file_manager.delete_item()
        mock_remove.assert_called_with("test_item")
        mock_print.assert_called_with("Элемент test_item удален.")

    @patch("builtins.input", side_effect=["test_item", "new_test_item"])
    @patch("os.path.exists", return_value=True)
    @patch("os.path.isdir", return_value=True)
    @patch("shutil.copytree")
    @patch("builtins.print")
    def test_copy_item_folder(self, mock_print, mock_copytree, mock_isdir, mock_exists, mock_input):
        file_manager.copy_item()
        mock_copytree.assert_called_with("test_item", "new_test_item")
        mock_print.assert_called_with("Элемент test_item скопирован как new_test_item.")

    @patch("builtins.input", side_effect=["test_item", "new_test_item"])
    @patch("os.path.exists", return_value=True)
    @patch("os.path.isdir", return_value=False)
    @patch("shutil.copy")
    @patch("builtins.print")
    def test_copy_item_file(self, mock_print, mock_copy, mock_isdir, mock_exists, mock_input):
        file_manager.copy_item()
        mock_copy.assert_called_with("test_item", "new_test_item")
        mock_print.assert_called_with("Элемент test_item скопирован как new_test_item.")

    @patch("builtins.open", new_callable=mock_open, read_data='{"balance": 100, "purchases": []}')
    def test_load_account_data(self, mock_file):
        balance, purchases = file_manager.load_account_data()
        self.assertEqual(balance, 100)
        self.assertEqual(purchases, [])

    @patch("os.listdir", return_value=["file1.txt", "file2.txt", "dir1", "dir2"])
    @patch("builtins.open", new_callable=mock_open)
    @patch("os.path.isfile", side_effect=lambda x: x.endswith(".txt"))
    @patch("os.path.isdir", side_effect=lambda x: not x.endswith(".txt"))
    @patch("builtins.print")
    def test_save_directory_contents(self, mock_print, mock_isfile, mock_isdir, mock_open, mock_listdir):
        file_manager.save_directory_contents("listdir.txt")
        mock_open().write.assert_any_call("files: file1.txt, file2.txt\n")
        mock_open().write.assert_any_call("dirs: dir1, dir2\n")
        mock_print.assert_called_with("Содержимое текущей директории сохранено в listdir.txt.")

if __name__ == '__main__':
    unittest.main()
