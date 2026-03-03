data = ["1 строка\n", "2 строка\n"]

with open('example.txt', 'w', encoding='utf-8') as file:
    file.writelines(data)
    file.write("Доп часть текста")

print("типо все сощзданно .")

