import os
import shutil

# Перемещение файла в папку
if os.path.exists('example.txt'):
    if not os.path.exists('test_folder'):
        os.mkdir('test_folder')
    shutil.move('example.txt', 'test_folder/example_moved.txt')
    print("Файл перемещен в test_folder.")