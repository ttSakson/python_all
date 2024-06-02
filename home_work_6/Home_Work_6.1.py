
import string

user_letters = input("Enter your letters: ")
all_letters = string.ascii_letters  #використовуємо набір з модуля
first_letter, second_letter = user_letters.split('-')  #розділяємо отримані букви

first_letter = all_letters.index(first_letter)  #визначаємо індекс кожної букви
second_letter = all_letters.index(second_letter)
result = all_letters[first_letter:second_letter + 1]
# знаходимо різницю ":" через індекс та пишемо + 1 щоб врахувати індекс останньої букви
print(result)
