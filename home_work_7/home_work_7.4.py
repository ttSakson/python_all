def common_elements():
    div_3 = [num for num in range(100) if num % 3 == 0] #в проміжку до 100 генеруємо цифри які кратні 3
    div_5 = [num for num in range(100) if num % 5 == 0] #ті які кратні 5

    set_1 = set(div_3).intersection(set(div_5)) #операція з множинами, яка повертає нову множину що містить спільне для обох

    return set_1


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
