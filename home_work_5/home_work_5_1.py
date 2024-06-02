#Завдання: Ім'я змінної
# Змінна не може:
# починатися з цифри
# містити великі літери,
# пробіл і знаки пунктуації (взяти можна тут string.punctuation), окрім нижнього підкреслення "_".
# бути жодним із зареєстрованих слів.


import keyword
import string

user_text = input("Please, enter your text: ")
def is_valid_variable(user_text):
    if user_text[0].isdigit(): #перевірка чи індекс 1 слова є цілим числом
        return False
    if not user_text.islower(): #лише нижній регістр
        return False
    if user_text.count('_') > 1: #чи є більше 1 нижнього підкреслення
        return False
    if user_text in keyword.kwlist: #чи є у тексті слова з ключових слів Пайтон
        return False

    for char in user_text: #цикл для перевірки кожного символу у введеному тексті
        if char != '_' and (char in string.punctuation or char == ' '):
            return False
    return True

print(is_valid_variable(user_text))

#умова якщо у рядку є символи зі string.punctuation або символ є ' ' (пробілом), і при цьому чи не є символ "_"
# (бо 1 "_" такий нам дозволено в умові завдання).


# --------------------------------
# V2
# import string
# import keyword
#
# user_text = input("Please, enter your text: ")
# valid_variable = True
#
# if user_text[0].isdigit() or not user_text.islower() or user_text.count('_') > 1 or user_text in keyword.kwlist:
#     valid_variable = False
# else:
#     for char in user_text:
#         if char != '_' and char in string.punctuation or char == ' ':
#             valid_variable = False
#             break
#
# print(valid_variable)



