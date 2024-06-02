my_list = [1, 5, 8, 3]
num_str = ''.join(map(str, my_list))
# join обєднує все в 1 рядок.
#map дія дял кожного елементу з масиву
number = int(num_str)


def add_one(number):
    number += 1
    return number


result_number = add_one(number)
result_str = str(result_number)
result_list = [int(char) for char in result_str]

print(result_list)
