def remove_keys_below_threshold(dict1, threshold):
    result = {}
    for key, value in dict1.items():
        if threshold <= value:
            result[key] = value
    return result

dict1 = {"a": 12, "j": 4, "u": 23}
threshold = int(input("Please enter a number: "))
print(remove_keys_below_threshold(dict1, threshold))