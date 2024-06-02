user_input = input("Enter your number: ")
numbers = [int(char) for char in user_input] #створила список де окремо кожен символ з рядка перетворити в ціле число
def multiply_numbers(numbers): #функція множення
    result = 1
    for num in numbers:
        result *= num #результат множить кожне число зі списку numbers і зберігає результат у змінній result
    return result

result = multiply_numbers(numbers) #виклик функції

while result > 9:
    numbers = [int(char) for char in str(result)]  #поки результат більше 9, ми знову кожне число розділяємо між собою
    result = multiply_numbers(numbers)

print("Result:", result)

