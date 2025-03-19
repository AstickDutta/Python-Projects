# Python Dictionary Methods Cheat Sheet with Examples

print("1. dict.get(key, default): Retrieves the value for a key, returns default if key is missing")
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict.get("name"))  # Alice
print(my_dict.get("age"))  # 25
print(my_dict.get("country", "USA"))  # USA (default value)

print("\n2. dict.keys(): Returns all keys in the dictionary")
my_dict = {"a": 1, "b": 2, "c": 3}
print(my_dict.keys())  # dict_keys(['a', 'b', 'c'])
for key in my_dict.keys():
    print(key, end=" ")  # a b c

print("\n\n3. dict.values(): Returns all values in the dictionary")
my_dict = {"x": 10, "y": 20, "z": 30}
print(my_dict.values())  # dict_values([10, 20, 30])
for value in my_dict.values():
    print(value, end=" ")  # 10 20 30

print("\n\n4. dict.items(): Returns all key-value pairs as tuples")
my_dict = {"name": "Bob", "age": 30, "city": "Chicago"}
print(my_dict.items())  # dict_items([('name', 'Bob'), ('age', 30), ('city', 'Chicago')])
for key, value in my_dict.items():
    print(f"{key}: {value}")

print("\n5. dict.update(new_dict): Updates the dictionary with another dictionary")
my_dict = {"a": 1, "b": 2}
my_dict.update({"b": 10, "c": 3})
print(my_dict)  # {'a': 1, 'b': 10, 'c': 3}

print("\n6. dict.pop(key, default): Removes the key and returns its value")
my_dict = {"a": 1, "b": 2, "c": 3}
print(my_dict.pop("b"))  # 2
print(my_dict)  # {'a': 1, 'c': 3}
print(my_dict.pop("z", "Not Found"))  # Not Found

print("\n7. dict.popitem(): Removes and returns the last key-value pair")
my_dict = {"x": 100, "y": 200, "z": 300}
print(my_dict.popitem())  # ('z', 300)
print(my_dict.popitem())  # ('y', 200)
print(my_dict)  # {'x': 100}

print("\n8. dict.clear(): Removes all elements from the dictionary")
my_dict = {"p": 1, "q": 2, "r": 3}
my_dict.clear()
print(my_dict)  # {}

print("\n9. dict.copy(): Returns a shallow copy of the dictionary")
original = {"a": 10, "b": 20}
copy_dict = original.copy()
print(copy_dict)  # {'a': 10, 'b': 20}
copy_dict["c"] = 30
print(original)  # {'a': 10, 'b': 20} (original is unchanged)

print("\n10. dict.setdefault(key, default): Returns value of key, if missing, sets it to default")
my_dict = {"name": "John"}
print(my_dict.setdefault("name", "Mike"))  # John
print(my_dict.setdefault("age", 25))  # 25
print(my_dict)  # {'name': 'John', 'age': 25}

print("\n11. Creating a dictionary using dict.fromkeys(keys, default_value)")
keys = ["id", "name", "age"]
default_value = "Unknown"
new_dict = dict.fromkeys(keys, default_value)
print(new_dict)  # {'id': 'Unknown', 'name': 'Unknown', 'age': 'Unknown'}

print("\n12. Using dictionary comprehension to create a dictionary")
squares = {x: x*x for x in range(1, 6)}
print(squares)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

print("\n13. Merging two dictionaries using | operator (Python 3.9+)")
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 10, "c": 3}
merged_dict = dict1 | dict2
print(merged_dict)  # {'a': 1, 'b': 10, 'c': 3}
