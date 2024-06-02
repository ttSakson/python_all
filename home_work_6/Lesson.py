# binary_data = bytes([0b01101000, 0b01100101, 0b01101100, 0b01101100, 0b01101111])
# decoded_text = binary_data.decode('utf-8')
# print(decoded_text)
#
# num = int(input("Enter number: "))
# nums = 12, int(input("Enter number: ")), num
# print(nums)



human = {"name": "Alexander",
        "lastname": "Glock",
        "age": 36,
        "address": {"street": "Lisova", "house": 87, "flat": 705}
}

house = human["address"]["house"]
print(house) # виведе: 87

# Міняємо значення для квартири
human["address"]["flat"] = 700
print(human["address"]["flat"])