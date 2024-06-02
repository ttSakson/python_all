nums_str = input("Enter your numbers: ")
nums_list = [float(num) for num in nums_str.replace(',', ' ').split() if num.strip()]

def difference(nums_list):
    if not nums_list:
        return 0
    max_num = max(nums_list)
    min_num = min(nums_list)
    result = max_num - min_num
    return round(result, 2)

result = difference(nums_list)
print("Result: ", result)


