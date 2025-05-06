def group_element(dict1):
    new_dict = {}
    for item in dict1:
        list1 = []
        if dict1[item] not in new_dict:
            new_dict[dict1[item]] = [item]
        else:
            for in_items in new_dict[dict1[item]]:
                list1.append(in_items)
            list1.append(item)
            new_dict[dict1[item]] = list1
    return new_dict

dict1 = {"a": 1, "b": 3, "d": 1, "t": 7, "e":3}
print(group_element(dict1))