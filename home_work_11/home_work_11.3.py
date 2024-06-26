# v1
# def is_even(number):
#     last_digit = str(number)[-1]
#     return last_digit in '02468'

# assert is_even(2494563894038**2) == True, 'Test1'
# assert is_even(1056897**2) == False, 'Test2'
# assert is_even(24945638940387**3) == False, 'Test3'
# print("Ok!")

#v2 знайшла інший варіант рішення в інтернеті і спробувала його розібрати.
''''
парні числа в бінарній системі завжди закінчуються на 0. наприклад, цифра 2 - 00000010, де останній біт є нулем
непарні числа у бінарній системі  мають останній біт 1. наприклад, цифра 3 має вигляд: 00000011
'''''


def is_even(number):
    return (number & 1) == 0

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print("Ok!")

'''
у коді порівнюютсья біти обох чисел
наприклад, наше ціле число 2 та число 1 = 00000010 та 00000001 = 00000000 
(останні біти двійки та одинці порівнюються: 0 та 1 = 0)
В результаті буде 0 == 0  і це повертає True, бо якщо хоча б один з бітів є 0, результатом буде 0.
3 та 1 = 00000011 та 00000001 = 00000001 (останні біти обох чисел порівнюються: 1 & 1 = 1)
в результаті  1 == 0 тому буде False, оскільки обидва біти є 1, результатом буде 1.

проводити поріняння з цифрою 1 найлегше, тому що 1 - це 00000001, де усе є нулі, окрім останнього біту. Тому ми у цьому випадку 
практично перевіряємо лише останній біт числа.

'''




