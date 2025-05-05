# def remove_keys_below_threshold(dict1, threshold):
#     result = {}
#     for key, value in dict1.items():
#         if threshold <= value:
#             result[key] = value
#     return result

# dict1 = {"a": 12, "j": 4, "u": 23, "p": 89, "l": 30}
# threshold = int(input("Please enter a number: "))
# print(remove_keys_below_threshold(dict1, threshold))


def remove_keys_below_threshold(dict1, threshold):
    result = {}
    for item in dict1:
        if threshold < dict1[item]:
            result[item] = dict1[item]
    return result

dict1 = {"a": 12, "j": 4, "u": 23, "p": 89, "l": 30}
threshold = int(input("Please enter a number: "))
print(remove_keys_below_threshold(dict1, threshold))

