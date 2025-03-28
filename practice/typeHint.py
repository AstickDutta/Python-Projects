from typing import List, Tuple, Dict, Union

# List Examples
marks: List[int] = [85, 90, 78, 92]
print(marks)

names: List[str] = ["Astick", "John", "Emma"]
print(names)

mixed: List[Union[int, str]] = [1, "hello", 42, "world"]
print(mixed)

# Tuple Examples
employee: Tuple[int, str, str] = (101, "Astick", "Developer")
print(employee)

data: Tuple[int, float, str] = (1, 3.14, "Pi")
print(data)

# Dictionary Examples
students: Dict[int, str] = {1: "John", 2: "Alice", 3: "Bob"}
print(students)

info: Dict[str, Union[str, int]] = {"name": "Astick", "age": 25, "city": "London"}
print(info)

# Union Example
identifier: Union[int, str] = "ABC123"
print(identifier)

identifier = 9876
print(identifier)

def get_id(value: Union[int, str]) -> str:
    return f"Your ID is {value}"

print(get_id(12345))
print(get_id("EMP456"))

# Function Example
def get_scores(students: Dict[str, List[int]]) -> None:
    for name, scores in students.items():
        print(f"{name}: {scores}")

data = {
    "Astick": [85, 90, 88],
    "John": [75, 80, 72]
}

get_scores(data)