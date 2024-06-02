# Список із 3 елементів


import random

numbers = [random.randint(3, 10)]
NUMS_SIZE = 10

for i in range(NUMS_SIZE):
    numbers.append(random.randint(3, 10))

# Створюємо новий список з 3 останніми елементами першого списку
new_list = [numbers[-1], numbers[-2], numbers[-3]]

print("Список випадкових чисел:", numbers)
print("Новий список:", new_list)
