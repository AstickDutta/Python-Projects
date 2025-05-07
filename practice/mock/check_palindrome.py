# def check_palindrome(number):
#     temp = number
#     mod = 0
#     res = 0

#     while number > 0:
#         mod = number % 10
#         res = (res * 10) + mod
#         number //= 10
#     return "It is a palindrome" if res == temp else "given number is not a palindrome"
# number = int(input("Please enter a number : "))
# print(check_palindrome(number) )


# def check_palindrome(original_number):
#     temp_number = original_number
#     reversed_number = 0
#     while temp_number > 0:
#         last_digit = temp_number % 10
#         reversed_number = reversed_number * 10 + last_digit
#         temp_number //= 10
#     return "Given value is palindrome" if reversed_number == original_number else "Given value is not a palindrome"

# original_number = int(input("Please enter a number : "))
# print(check_palindrome(original_number))

# def common_ele(list1):
#     common = list1[0]
#     for sublist in list1[1:]:
#         temp = []
#         for num in common:
#             if num in sublist:
#                 temp.append(num)
#             common = temp
#     return common

# list1 = [[2, 5, 7], [3, 2, 8], [56, 2, 5], [3, 6, 2]]
# print(common_ele(list1))


# def palindrome(original_number):
#     temp_number = original_number
#     reversed_number = 0

#     while temp_number > 0:
#         last_digit = temp_number % 10
#         reversed_number = reversed_number * 10 + last_digit
#         temp_number //= 10
#     return "it is a palindrome" if reversed_number == original_number else "it is not a palindrome"

# original_number = int(input("Please enter number : "))
# print(palindrome(original_number))
