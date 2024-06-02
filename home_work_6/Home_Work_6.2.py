num = int(input("Enter your number: "))

if num < 0 or num > 8640000:
    print("Error")
else:
    days = num // 86400
    num %= 86400

    hours = num // 3600
    num %= 3600

    minutes = num // 60
    seconds = num % 60

print(f"Result: {days} день, {hours:02}:{minutes:02}:{seconds:02}")
