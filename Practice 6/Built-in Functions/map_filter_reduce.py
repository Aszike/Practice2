from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# map: возведение в квадрат
squared = list(map(lambda x: x**2, numbers))

# filter: только четные
evens = list(filter(lambda x: x % 2 == 0, numbers))

# reduce: сумма всех элементов
total_sum = reduce(lambda x, y: x + y, numbers)

print(f"Квадраты: {squared}")
print(f"Четные: {evens}")
print(f"Сумма: {total_sum}")