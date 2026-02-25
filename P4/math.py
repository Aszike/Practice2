import math

def degree_to_radian(degree):
    return degree * (math.pi / 180)

deg = 90
print(f"{deg} градусов в радианах: {degree_to_radian(deg):.6f}")

# Пример с Random: случайное число от 1 до 10
import random
print("Случайное число:", random.randint(1, 10))