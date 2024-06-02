
import string

def is_palindrome(text):
    text = text.lower() #перевести текст у нижній регістр


    text = ''.join(char for char in text if char.isalnum())
#'' - видалити всі пробіли
#join - конкатенція (тобто об'єднання всіх символів в один рядок)
#цикл пройтись по кожному символу з рядка у тексті
#char.isalnum() умова перевіряє, чи є кожен символ буквою/цифрою


    return text == text[::-1]
#[::-1] тобто рухаємося у тексті по індексу кожного символа починаючи з кінця і до початку.
# отже, чи текст == (такий самий/дорівнює) тексту, у якого кроки ідуть з кінця, з останнього індексу


# Тестування функції
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")

