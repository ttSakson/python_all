# Знайти суму елементів із парними індексами

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pair_index = numbers[:: 2] #знайшла усі парні індекси списку
sum_pair_elements = sum(pair_index) #знайти суму елементів просто через sum(сума)
print(pair_index)
print(sum_pair_elements)
result = sum_pair_elements * numbers[-1]
print(result)
