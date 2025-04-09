# # check odd number

# number = int(input("Please enter a number: "))

# if number % 2 != 0:
#     print(f"Given number {number} is a odd number")
# else:
#     print(f"Given number {number} is not a odd number")


# number = int(input("Please enter a number: "))

# if number % 2 == 0:
#     print(f"Given number {number} is a even number")
# else:
#     print(f"Given number {number} is not a even number")


# # print only even numbers in between 1 to 100

# for i in range(1 , 100):
#     if i % 2 != 0:
#         print(i)

# # check prime number

# number = int(input("Please enter a number: "))

# if number == 2:
#     print("Given number is a prime number")

# elif number < 2:
#     print("Given number is not a prime number")

# else:
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             print(f"Given number {number} is not a prime number")
#     else:
#         print(f"Given number {number} is a prime number")

# def my_decorator(func):
#     def wrapper():
#         print("calling before that function")
#         func()
#         print("calling after the function")
#     return wrapper

# @my_decorator
# def sayHello():
#     print("Hii there")
# sayHello()

# word = input("Please enter a word: ")

# if word == word[:: -1] :
#     print("Given word is a palindrome")
# else:
#     print("Given string is not a palindrome")


# str1 = "Python"
# str2 = "yhtonp"

# str1 = str1.lower()
# str2 = str2.lower()

# if len(str1) != len(str2):
#      print("The strings have different lengths and cannot be anagrams.")

# else:
#     charStr1 = {}
#     charStr2 = {}

#     for char in str1:
#         if char in charStr1:
#             charStr1[char] = +1
#         else:
#             charStr1[char] = 1

#     for char in str2:
#         if char in charStr2:
#             charStr2[char] = +1
#         else:
#             charStr2[char] = 1

#     if charStr1 == charStr2:
#         print("Given word is an Anagrams")

#     else:
#         print("Given word is not an Anagrams")


# string = "m d m"
# char = "a"
# result = ""

# for i in string:
#     if i == " ":
#         i = char
#     result += i

# print("After removed space string result will be", result)

# str = "Python"

# reverse = str[::-1]

# print(reverse)

# def reverse_str(s):
#     reversed_string = ""

#     for char in s:
#         reversed_string = char + reversed_string
#     return reversed_string

# input_string = input("Enter a string: ")
# output_string = reverse_str(input_string)

# print("Original string", input_string)
# print("Reversed string", output_string)


# number = 1221

# str_number = str(number)

# if str_number == str_number[:: -1]:
#     print("Given number is a Palindrome")
# else:
#     print("Given number is not a Palindrome")


# countVowel = input("Please some word or sentence: ")
# vowel = "aeiouAEIOU"

# count = 0

# for char in countVowel:
#     if char in vowel:
#         count += 1
# print(count)

# factorialNumber = int(input("please put a number: "))

# fact = 1
# i = 1

# while i <= factorialNumber:
#     fact *= i
#     i += 1
# print(fact)

# ls = [1,2,2,3,42,2,4,6, 8,4]
# newLst = []

# for i in ls:
#     if i not in newLst:
#         newLst.append(i)

# print(newLst)

# li_Element = [2,4,6,9,10,45]

# if not li_Element:
#     print("given elements are empty")

# max_element = li_Element[0]

# for ele in li_Element:
#     if ele > max_element:
#         max_element = ele
# print(f"largest element form the given elements is {max_element}")


# le_element = [2,3,4,6,7,8,934]

# if not le_element:
#     print("it is not list")

# min_element = le_element[0]

# for ele in le_element:
#     if ele < min_element:
#         min_element = ele
# print(f"smallest number from given list is {min_element}")

number = int(input("Please enter a digit: "))

num_digit = str(number)
digit_num = 0

for digit in num_digit:
    digit_num += int(digit)

print(f"Sum of given value {num_digit}'s addition is {digit_num}")