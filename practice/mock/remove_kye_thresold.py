def remove_keys_below_threshold(dict1, threshold):
    result = {}
    for key, value in dict1.items():
        if threshold <= value:
            result[key] = value
    return result

dict1 = {"a": 12, "j": 4, "u": 23, "p": 89, "l": 30}
threshold = int(input("Please enter a number: "))
print(remove_keys_below_threshold(dict1, threshold))


def remove_keys_below_threshold(dict1, threshold):
    result = {}
    for item in dict1:
        if threshold < dict1[item]:
            result[item] = dict1[item]
    return result

dict1 = {"a": 12, "j": 4, "u": 23, "p": 89, "l": 30}
threshold = int(input("Please enter a number: "))
print(remove_keys_below_threshold(dict1, threshold))

def factorial(number):
    fact = 1
    for ele in range(1, number + 1):
        fact *= ele
    return fact

def check_strong_number(number):
    sum = 0
    str_number = str(number)

    for num in str_number:
        sum += factorial(int(num))
    return "Given number is strong number.." if sum == number else "Given number is not a prime number.."
    # if sum == number:
    #     print("Given number is strong number..")
    # else:
    #     print("Given number is not a prime number..")

number = int(input("Please enter a number: "))
print(check_strong_number(number))


def check_armstrong(number):
    str_number = str(number)
    len_number = len(str_number)
    armstrong_number = 0
    for num in str_number:
        armstrong_number += int(num) ** len_number
    return "Given number is armstrong number " if armstrong_number == number else "Given number is not a armstrong number"
    # if armstrong_number == number:
    #     print("Given number is a armstrong number")
    # else:
    #     print("Given number is not a armstrong number")

number = int(input("please enter a value: "))
print(check_armstrong(number))


s1 = input("Please enter a value for s1: ")
s2 = input("Please enter a value for s2: ")

if len(s1) != len(s2):
    print("it cant be anagram")
else:
    str1 = {}
    str2 = {}

    for char in s1:
        if char in str1:
            str1[char] += 1
        else:
            str1[char] = 1

    for char in s2:
        if char in str2:
            str2[char] += 1
        else:
            str2[char] = 1

    if str1 == str2:
        print("Give values are anagram")
    else:
        print("given values are not an anagram")


def factorial(number):
    fact = 1
    while number > 0:
        fact *= number
        number -= 1
    return f"given number  factorial value is {fact}"

number = 5
print(factorial(number))


def list_dict(dict1):
    new_dict = {}
    for items in dict1:
        list1 = []
        if dict1[items] not in new_dict:
            new_dict[dict1[items]] = [items]
        else:
            for in_item in new_dict[dict1[items]]:
                list1.append(in_item)
            list1.append(items)
            new_dict[dict1[items]] = list1

    return new_dict

dict1 = {"a": 1, "b":1, "d":8, "t":7}
#       {1: ['a', 'b'], 8: ['d'], 7: ['t']}
print(list_dict(dict1))

def list_dict(dict1):
    new_dict = {}
    for key, value in dict1.items():
        if value not in new_dict:
            new_dict[value] = [key]
        else:
            new_dict[value].append(key)
    return new_dict

dict1 = {"a": 1, "b": 3, "d": 1, "t": 7, "e":3}
print(list_dict(dict1))

# {1: ['a', 'd'], 2: ['b', 'e'], 8: ['d'], 7: ['t']}

def check_value(dict1):
    new_dict = {}
    for item in dict1:
        list1 = []
        if dict1[item] not in new_dict:
            new_dict[dict1[item]] = [item]
        else:
            for in_item in new_dict[dict1[item]]:
                list1.append(in_item)
            list1.append(item)
            new_dict[dict1[item]] = list1
    return new_dict

dict1 = {"a": 1, "b": 3, "d": 1, "t": 7, "e":3}
print(check_value(dict1))
