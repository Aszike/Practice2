import os

# Создание папки
dir_name = "test_folder"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
    print(f"Папка {dir_name} создана.")

# Список всех файлов и папок в текущей директории
print("Список объектов:", os.listdir('.'))
