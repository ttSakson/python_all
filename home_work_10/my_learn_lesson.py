# def additional_logic(func):
#     def wrapper():
#         print("Some logic 1")
#         func()
#         print("Dome logic 2)")
#     return wrapper
#
# @additional_logic
# # декоратор - це функція яка містить замиканя
# def hello():
#     print("Hello!")
#
#
# hello()
import math
##########################3

# def check_permissions(func):
#     def wrapper(role):
#         if role == 'admin':
#             print("Permissions granted!")
#             func(role)
#         else:
#             print("Permission denied!")
#     return wrapper
#
# @check_permissions
# def get_secret_information(user_role):
#     print(f"Hi {user_role}, this is secret information.")
#
#
# get_secret_information("user")
# get_secret_information("admin")

##########################

# def start(func):
#     def wrapper(name):
#         print("Hello ", end="")
#         func(name)
#     return wrapper
# #
# #
# # def end(func):
# #     def wrapper(name):
# #         print("Goodbye ", end="")
# #         func(name)
# #     return wrapper
#
# @start
# @end
# def hello(name):
#     print(name)
#
# hello("May")


##########################

# def count_up_to(max):
#     count = 1
#     while count <= max:
#         yield count
#         count += 1
#
# # Використання генератора
# counter = count_up_to(5)
# for num in counter:
#     print(num)

# def my_generator():
#     yield 1
#     yield 2
#     yield 3
#
# gen = my_generator()
#
# print(next(gen))  # Вивід: 1
# print(next(gen))  # Вивід: 2
# print(next(gen))



##########################
# Напишіть рекурсивну функцію, яка приймає одновимірний масив із 100 цілих чисел заповнених випадковим чином
# і знаходить позицію, з якої починається послідовність з 10 чисел, сума яких мінімальна.

# import random
# #створення масиму з випадкових 100 чисел
# array = [random.randint(1,100) for _ in range(100)]
# print(array)
#
# def find_min_subarray(array, start=0, min_sum=float('inf'), min_index=0):
#     if start > len(array) - 10:
#         return min_index, min_sum
#
# #Рекурсивна функція. Базовий випадок: якщо залишилося менше ніж 10 чисел, повернути індекс і суму підмасиву.
#
#     current_sum = sum(array[start:start+10])
#
# # Рекурсивний випадок: обчислити суму поточного підмасиву і порівняти з мінімальною сумою,
# # знайденої в рекурсивному виклику.
#
#     if current_sum < min_sum:
#         min_sum = current_sum
#         min_index = start
#
#     return find_min_subarray(array, start + 1, min_sum, min_index)
#
# min_index, min_sum = find_min_subarray(array)
# print(f"Початкова позиція: {min_index}, Мінімальна сума: {min_sum}")
# Пояснення коду
# Базовий випадок: Якщо залишилося менше ніж 10 чисел, повертаємо індекс і мінімальну суму.
# Рекурсивний випадок: Обчислюємо суму поточного підмасиву і порівнюємо з мінімальною сумою.
# Викликаємо функцію для наступного підмасиву.


# v2
import random
def find_min_sum_index(numbers: list[int], start_index, end_index, min_sum=math.inf, min_index=0):
# записуємо у мінімальну суму +безкінечність (щоб було з чим порівняти, бо з самого початку може
# бути будь яка мінімальна сума)
#[список чисел, початковий індекс, кінцевий індекс, мінімальна сума чисел безкінечна, мінімальний індекс є нуль]
    if end_index < len(numbers):
        current_sum = sum(numbers[start_index: end_index+1])

        if current_sum < min_sum:
            min_sum = current_sum
            min_index = start_index

        start_index += 1
        end_index += 1

        print(f"Current sum: {current_sum} and Min sum: {min_sum}")

        return find_min_sum_index(numbers, start_index, end_index, min_sum, min_index)

    return min_index

nums = [random.randint(1,10) for _ in range(10)]
print(nums)
result = find_min_sum_index(nums, 0, 1)
print(result)