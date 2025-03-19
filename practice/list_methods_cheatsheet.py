# Python List Methods Cheat Sheet with Examples

print("1. append(item): Adds an item to the end of the list")
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # [1, 2, 3, 4]
my_list.append("Hello")
print(my_list)  # [1, 2, 3, 4, 'Hello']
my_list.append([5, 6])
print(my_list)  # [1, 2, 3, 4, 'Hello', [5, 6]]

print("\n2. extend(iterable): Extends the list by adding elements from an iterable")
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list)  # [1, 2, 3, 4, 5, 6]
my_list.extend("abc")
print(my_list)  # [1, 2, 3, 4, 5, 6, 'a', 'b', 'c']
my_list.extend((7, 8))
print(my_list)  # [1, 2, 3, 4, 5, 6, 'a', 'b', 'c', 7, 8]

print("\n3. insert(index, item): Inserts an item at a specific index")
my_list = [1, 2, 3]
my_list.insert(1, "A")
print(my_list)  # [1, 'A', 2, 3]
my_list.insert(0, 100)
print(my_list)  # [100, 1, 'A', 2, 3]
my_list.insert(len(my_list), "End")
print(my_list)  # [100, 1, 'A', 2, 3, 'End']

print("\n4. remove(item): Removes the first occurrence of an item")
my_list = [1, 2, 3, 4, 2, 5]
my_list.remove(2)
print(my_list)  # [1, 3, 4, 2, 5]
my_list.remove(5)
print(my_list)  # [1, 3, 4, 2]
# my_list.remove(10)  # ValueError: 10 is not in the list

print("\n5. pop(index): Removes and returns an item at a given index (default is last)")
my_list = [1, 2, 3, 4, 5]
print(my_list.pop())  # 5
print(my_list)  # [1, 2, 3, 4]
print(my_list.pop(1))  # 2
print(my_list)  # [1, 3, 4]

print("\n6. index(item): Returns the index of the first occurrence of an item")
my_list = [10, 20, 30, 40, 50]
print(my_list.index(30))  # 2
print(my_list.index(10))  # 0
# print(my_list.index(100))  # ValueError: 100 is not in the list

print("\n7. count(item): Counts occurrences of an item in the list")
my_list = [1, 2, 2, 3, 4, 2, 5]
print(my_list.count(2))  # 3
print(my_list.count(5))  # 1
print(my_list.count(10))  # 0

print("\n8. sort(): Sorts the list in ascending order")
my_list = [3, 1, 4, 2, 5]
my_list.sort()
print(my_list)  # [1, 2, 3, 4, 5]
my_list = ["banana", "apple", "cherry"]
my_list.sort()
print(my_list)  # ['apple', 'banana', 'cherry']
my_list = [5, 3, 1, 4, 2]
my_list.sort(reverse=True)
print(my_list)  # [5, 4, 3, 2, 1]

print("\n9. reverse(): Reverses the list")
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)  # [5, 4, 3, 2, 1]
my_list = ["a", "b", "c"]
my_list.reverse()
print(my_list)  # ['c', 'b', 'a']
my_list = [10, 20, 30]
my_list.reverse()
print(my_list)  # [30, 20, 10]

print("\n10. copy(): Returns a shallow copy of the list")
my_list = [1, 2, 3]
copy_list = my_list.copy()
print(copy_list)  # [1, 2, 3]
copy_list.append(4)
print(copy_list)  # [1, 2, 3, 4]
print(my_list)  # [1, 2, 3] (original list remains unchanged)

print("\n11. clear(): Removes all elements from the list")
my_list = [1, 2, 3, 4, 5]
my_list.clear()
print(my_list)  # []

print("\n12. List Comprehension: Creating lists in a concise way")
squared = [x ** 2 for x in range(5)]
print(squared)  # [0, 1, 4, 9, 16]
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)  # [0, 2, 4, 6, 8]
words = ["hello", "world", "python"]
capitalized_words = [word.upper() for word in words]
print(capitalized_words)  # ['HELLO', 'WORLD', 'PYTHON']
