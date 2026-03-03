try:
    with open('example.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print("Содержимое файла:")
        print(content)
except FileNotFoundError:
    print("Файл не найден. Сначала запустите write_files.py")