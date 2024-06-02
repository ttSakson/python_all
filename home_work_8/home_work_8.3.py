my_list = [1, 25, 856, 2425, 2, 1, 3, 457, 3]

def find_unique_value(my_list):
    counts = {} #буде словник в якому зберігатимуться: ключ - то цифра, а значення - її кількість
    for number in my_list:  #проходимось циклом для кожного числа у списку з цифрами
        if number in counts: # кожне число добавляємо в словник
            counts[number] += 1 # якщо число в словнику вже є, то добавляємо в рахунок ще одне
        else:
            counts[number] = 1 #умова якщо такого числа у словнику немає, то створюється ключ зі значенням 1

    for key, value in counts.items(): #метод словника .items() щоб повернути набір ключ, значень
        if value == 1: #але нам треба лише один ключ (та єдина унікальна цифра яка є лише 1 раз)
            return key


unique_number = find_unique_value(my_list)
print(unique_number)


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")
