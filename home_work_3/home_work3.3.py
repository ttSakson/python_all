# Ваша програма повинна вміти розділяти один список на два та помістити їх у новий список.
# Тобто, в результаті повинен вийти список із 2-х списків.

# task.1 У списку парна кількість елементів.
my_list = [10, 20, 30, 40, 50, 60, 70, 80]
length = len(my_list)
print(length)
first_list = my_list[:4]
second_list = my_list[4:8]
print(first_list)
print(second_list)

my_new_list = [first_list, second_list]
print(my_new_list)


# task.2 У списку непарна кількість елементів.
my_list = [10, 20, 30, 40, 50]
length = len(my_list) // 2
print(length)
first_list = my_list[:3]
second_list = my_list[3:5]
print(first_list)
print(second_list)

my_new_list = [first_list, second_list]
print(my_new_list)


# task.3 Список порожній
my_list = []
length = len(my_list)
print(length)
my_new_list = [[], my_list]
print(my_new_list)
