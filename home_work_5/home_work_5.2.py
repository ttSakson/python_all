#Модифікувати калькулятор
#безкінечний цикл попросити ввести значення поки не буде ведене якесь значення...


#довго мучилась з тими зовнішніми та внутрішніми циклами, але результат того вартує :)

while True: #відкрила зовнішній цикл передумови щоб програма повторювалась звідси
    while True: #перший внутрішній цикл для введення числа користувачем
        try:
            print("Please, enter your first number: ")
            num1 = float(input()) #ставлю у float, щоб програма приймала цілі та числа з плаваючою комою
            break
        except ValueError:
            print("Choose only numbers.")#я поставила умову, щоб користувач міг вводити лише цифри і програма при цьому не ламалась

    while True: #ще один цикл уже для наступнго числа
        try:
            print("Please, enter your second number: ")
            num2 = float(input())
            break
        except ValueError:
            print("Choose only numbers.")

    while True:
        print("Please, choose an action:+, -, *, /")
        action = input()
        if action in ['+', '-', '*', '/']:
            break
        else:
            print("Invalid operation.")

    if action == "+":
        result = num1 + num2
    elif action == "-":
        result = num1 - num2
    elif action == "*":
        result = num1 * num2
    elif action == "/":
        while num2 == 0: #ще один внутрішній цикл: поки друге число дорівнює нулю, буде помилка, тому...
            print("Error. Your second number is zero.")
            while True:
                try:
                    num2 = float(input("Please, enter a non-zero second number: ")) #тому я не хотіла, щоб програма ламалась, або щоб програма поверталась до зовнішнього циклу.
                    break #я хочу щоб користувач мав можливість знову ввести своє друге число, тому тут цикл завершується до вибору другого числа
                except ValueError:
                    print("Please choose only numbers.") #не забуваю про умову щоб користувач вводив лише цифри і все працювало ок
        result = num1 / num2 #ну і звісно що якщо у нас немає нуля, то виконуєтсья наше ділення
        correct_operation = True

    if result is not None and result == int(result): #не знаю чи це обовязково, але якщо результат є цілим числом, то я захотіла щоб воно так і відображалось для користувача
        result = int(result)
        print("Result: ", result)

    while True: #ще один цикл для правильного введеня
        choice_input = input("Do you want to continue? (yes/no): ")
        if choice_input.lower() == "no" or choice_input.lower() == "n":
            print("Program finished.")
            exit() #думаю що писати break не логічно, бо користувач завершив роботу з калькулятором.
        elif choice_input.lower() == "yes" or choice_input.lower() == "y":
            break #користувач продовжує роботу з калькулятором, отже тут ми виходимо з цього циклку і повертаємось до самого першого, зовнішнього циклу.
        else:
            print("Please, enter only 'yes' or 'no'.")
        continue #внутрішній цикл продовжується, щоб користвач ввів лише потрібні нам yes, y, no, n







