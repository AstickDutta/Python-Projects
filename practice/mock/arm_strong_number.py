def arm_strong_number(number):
    str_number = str(number)
    len_number = len(str_number)
    arm_strong = 0

    for ele in str_number:
        arm_strong += int(ele) ** len_number
    return "given number an armstrong number" if arm_strong == number else "Given number is not an armstrong number"

number = int(input("Please input a number: "))
print(arm_strong_number(number))