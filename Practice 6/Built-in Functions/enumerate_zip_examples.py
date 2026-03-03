names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

# enumerate: получение индекса и значения
print("Список студентов:")
for index, name in enumerate(names, start=1):
    print(f"{index}. {name}")

# zip: объединение двух списков
print("\nРезультаты:")
for name, score in zip(names, scores):
    print(f"{name}: {score} баллов")