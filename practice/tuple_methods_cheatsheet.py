# Python Tuple Methods Cheat Sheet with Examples

print("1. count(item): Counts the occurrences of an item in a tuple")
my_tuple = (1, 2, 3, 2, 4, 2, 5)
print(my_tuple.count(2))  # 3
print(my_tuple.count(5))  # 1
print(my_tuple.count(10))  # 0

print("\n2. index(item): Returns the index of the first occurrence of an item")
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple.index(30))  # 2
print(my_tuple.index(10))  # 0
# print(my_tuple.index(100))  # ValueError: 100 is not in the tuple

print("\n3. len(): Returns the length of a tuple")
my_tuple = (1, 2, 3, 4, 5)
print(len(my_tuple))  # 5
my_tuple = ()
print(len(my_tuple))  # 0
my_tuple = ("hello", "world")
print(len(my_tuple))  # 2

print("\n4. tuple(): Converts an iterable into a tuple")
my_list = [1, 2, 3, 4]
print(tuple(my_list))  # (1, 2, 3, 4)
my_string = "hello"
print(tuple(my_string))  # ('h', 'e', 'l', 'l', 'o')
my_set = {5, 6, 7}
print(tuple(my_set))  # (5, 6, 7)

print("\n5. min(): Returns the smallest element in a tuple")
my_tuple = (5, 3, 9, 1, 7)
print(min(my_tuple))  # 1
my_tuple = (-10, -5, 0, 5, 10)
print(min(my_tuple))  # -10
my_tuple = ('b', 'a', 'c')
print(min(my_tuple))  # 'a'

print("\n6. max(): Returns the largest element in a tuple")
my_tuple = (5, 3, 9, 1, 7)
print(max(my_tuple))  # 9
my_tuple = (-10, -5, 0, 5, 10)
print(max(my_tuple))  # 10
my_tuple = ('b', 'a', 'c')
print(max(my_tuple))  # 'c'

print("\n7. sum(): Returns the sum of all numeric elements in a tuple")
my_tuple = (1, 2, 3, 4, 5)
print(sum(my_tuple))  # 15
my_tuple = (10, -5, 5)
print(sum(my_tuple))  # 10
my_tuple = (100,)
print(sum(my_tuple))  # 100

print("\n8. sorted(): Returns a sorted list from the elements of a tuple")
my_tuple = (5, 3, 9, 1, 7)
print(sorted(my_tuple))  # [1, 3, 5, 7, 9]
my_tuple = ("banana", "apple", "cherry")
print(sorted(my_tuple))  # ['apple', 'banana', 'cherry']
my_tuple = (9, 7, 5, 3, 1)
print(sorted(my_tuple, reverse=True))  # [9, 7, 5, 3, 1]

print("\n9. Tuple Concatenation: Combining two tuples")
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(tuple1 + tuple2)  # (1, 2, 3, 4, 5, 6)
tuple3 = ("a", "b") + ("c", "d")
print(tuple3)  # ('a', 'b', 'c', 'd')
tuple4 = (10,) + (20, 30)
print(tuple4)  # (10, 20, 30)

print("\n10. Tuple Repetition: Repeating a tuple multiple times")
my_tuple = (1, 2, 3)
print(my_tuple * 3)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)
my_tuple = ("A", "B")
print(my_tuple * 2)  # ('A', 'B', 'A', 'B')
my_tuple = (0,)
print(my_tuple * 5)  # (0, 0, 0, 0, 0)

print("\n11. Tuple Unpacking: Assigning tuple elements to variables")
my_tuple = (10, 20, 30)
a, b, c = my_tuple
print(a, b, c)  # 10 20 30
my_tuple = ("apple", "banana", "cherry")
x, y, z = my_tuple
print(x, y, z)  # apple banana cherry
my_tuple = (1, 2, [3, 4])
a, b, c = my_tuple
print(a, b, c)  # 1 2 [3, 4]

print("\n12. Tuple Slicing: Extracting elements from a tuple")
my_tuple = (0, 1, 2, 3, 4, 5)
print(my_tuple[1:4])  # (1, 2, 3)
print(my_tuple[:3])   # (0, 1, 2)
print(my_tuple[-3:])  # (3, 4, 5)
