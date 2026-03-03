import os
import shutil

# Копирование
if os.path.exists('example.txt'):
    shutil.copy('example.txt', 'example_copy.txt')
    print("Файл скопирован.")

# Удаление
if os.path.exists('example_copy.txt'):
    os.remove('example_copy.txt')
    print("Копия удалена.")