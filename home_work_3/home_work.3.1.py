# Найпростіший калькулятор
#
# Я не впевнена чи обов'язково тут писати int чи float.
# Тому обрала float, щоб калькулятор спрацював на обидва варіанти.

print("Hello, User. Please, enter your first number: ")
num1 = float(input())
print("Please, enter your second number: ")
num2 = float(input())
print("Please, choose an action:+, -, *, /")
action = input()
result = None

# створила змінну result зі значенням None (тобто поки що без будь яких даних),
# бо інакше пайтон видає помилку, не розуміє, звідки взялась моя змінна безпосередньо в обчисленні.

#v1
if action == "+":
    result = num1 + num2
elif action == "-":
    result = num1 - num2
elif action == "*":
    result = num1 * num2
elif action == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error. Your second number is zero.")
else:
    print("Invalid operation.")

# через float результат завжди пише нецілим числом
# (навіть якщо користувач вводить обидва або одне з чисел цілим)
# тому я спробувала добавити нову умову.

if result is not None and result == int(result):
    result = int(result)

print("Result: ", result)

# v2

match action:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error. Your second number is zero.")
    case _:
        print("Invalid operation.")

if result is not None and result == int(result):
    result = int(result)

print("Result: ", result)
