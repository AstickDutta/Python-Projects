# Python Set Methods Cheat Sheet with Examples

print("1. set.add(element): Adds an element to the set")
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # {1, 2, 3, 4}
my_set.add(2)  # No duplicates in sets
print(my_set)  # {1, 2, 3, 4}
my_set.add(5)
print(my_set)  # {1, 2, 3, 4, 5}

print("\n2. set.remove(element): Removes an element from the set (Error if not found)")
my_set = {10, 20, 30, 40}
my_set.remove(20)
print(my_set)  # {10, 30, 40}
my_set.remove(40)
print(my_set)  # {10, 30}
# my_set.remove(50)  # KeyError: 50 (Uncomment to test error)

print("\n3. set.discard(element): Removes an element without an error if not found")
my_set = {100, 200, 300}
my_set.discard(200)
print(my_set)  # {100, 300}
my_set.discard(500)  # No error
print(my_set)  # {100, 300}
my_set.discard(100)
print(my_set)  # {300}

print("\n4. set.pop(): Removes and returns a random element")
my_set = {5, 10, 15, 20}
print(my_set.pop())  # Random element removed
print(my_set.pop())  # Another random element removed
print(my_set)  # Remaining set

print("\n5. set.clear(): Removes all elements from the set")
my_set = {1, 2, 3, 4}
my_set.clear()
print(my_set)  # set()

print("\n6. set.copy(): Returns a shallow copy of the set")
original_set = {1, 2, 3}
copy_set = original_set.copy()
print(copy_set)  # {1, 2, 3}
copy_set.add(4)
print(original_set)  # {1, 2, 3} (original remains unchanged)
print(copy_set)  # {1, 2, 3, 4} (copy modified)

print("\n7. set.union(set2): Returns a new set containing all unique elements")
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = set1.union(set2)
print(result)  # {1, 2, 3, 4, 5}
print(set1 | set2)  # Alternative way using `|`

print("\n8. set.intersection(set2): Returns a new set with common elements")
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.intersection(set2))  # {3, 4}
print(set1 & set2)  # Alternative way using `&`

print("\n9. set.difference(set2): Returns a new set with elements only in set1")
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.difference(set2))  # {1, 2}
print(set1 - set2)  # Alternative way using `-`

print("\n10. set.symmetric_difference(set2): Returns elements in either set but not both")
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1.symmetric_difference(set2))  # {1, 2, 5, 6}
print(set1 ^ set2)  # Alternative way using `^`

print("\n11. set.issubset(set2): Checks if all elements of set1 are in set2")
set1 = {1, 2}
set2 = {1, 2, 3, 4}
print(set1.issubset(set2))  # True
print({3, 5}.issubset(set2))  # False
print({}.issubset(set2))  # True (Empty set is a subset of any set)

print("\n12. set.issuperset(set2): Checks if set1 contains all elements of set2")
set1 = {1, 2, 3, 4}
set2 = {2, 3}
print(set1.issuperset(set2))  # True
print(set1.issuperset({5, 6}))  # False
print(set1.issuperset(set1))  # True (A set is a superset of itself)

print("\n13. set.isdisjoint(set2): Checks if two sets have no common elements")
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.isdisjoint(set2))  # True (No common elements)
print(set1.isdisjoint({2, 5}))  # False (2 is common)
print(set1.isdisjoint({}))  # True (Any set and empty set are disjoint)

print("\n14. set.update(set2): Adds all elements from another set")
set1 = {1, 2, 3}
set2 = {4, 5}
set1.update(set2)
print(set1)  # {1, 2, 3, 4, 5}

print("\n15. set.intersection_update(set2): Keeps only common elements")
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}
set1.intersection_update(set2)
print(set1)  # {3, 4}

print("\n16. set.difference_update(set2): Removes elements found in another set")
set1 = {1, 2, 3, 4}
set2 = {3, 4}
set1.difference_update(set2)
print(set1)  # {1, 2}

print("\n17. set.symmetric_difference_update(set2): Updates set with non-common elements")
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.symmetric_difference_update(set2)
print(set1)  # {1, 2, 4, 5}
