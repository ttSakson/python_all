print("Please, enter your number: ")
number = int(input())
n1 = number // 1000
n2 = number // 100 % 10
n3 = number // 10 % 10
n4 = number % 10

print(n1)
print(n2)
print(n3)
print(n4)

result = n4 * 1000 + n3 * 100 + n2 * 10 + n1
print(result)
