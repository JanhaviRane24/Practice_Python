# 2. Type Hints (Type Definitions)
# What are Type Hints?

# Type hints tell Python (and programmers) what type of value is expected.

# They improve readability and help IDEs catch mistakes.

# They do not force Python to use only that type.

# Variable Type Hint
age: int = 25
print(age)

# Meaning

# Variable : age

# Expected Type : int

# Value : 25

# Example

name: str = "Alice"

print(name)

# Output

# Alice

# Example

price: float = 99.99

print(price)

# Output

# 99.99

# Example

is_passed: bool = True

print(is_passed)

# Output

# True
# Function Type Hints

# Syntax

# def function_name(parameter: datatype) -> return_type:

# Example

def greet(name: str) -> str:
    return "Hello " + name

print(greet("Alice"))
# Step-by-Step
# Function called

# ↓

# name = "Alice"

# ↓

# Returns

# "Hello Alice"

# Output

# Hello Alice

# Example

def add(a: int, b: int) -> int:
    return a + b

print(add(10, 20))

# Step-by-Step

# a = 10

# b = 20

# 10 + 20

# ↓

# 30

# Output

# 30

# Example

def area(length: float, width: float) -> float:
    return length * width

print(area(5.5, 2))

# Output

# 11.0
# Important Note

# Python does not enforce type hints.

# Example

age: int = "Hello"

print(age)

# Output

# Hello

# Python runs this without an error, although a type checker would warn about it.

# 3. Advanced Type Hints (typing Module)

# Import

from typing import List, Tuple, Dict, Union

# These types describe more complex data structures.

# A. List

# A list containing only integers.

from typing import List

numbers: List[int] = [1, 2, 3, 4]

print(numbers)

# Output

# [1, 2, 3, 4]

# Another Example

names: List[str] = ["Alice", "Bob", "Charlie"]

print(names)

# Output

# ['Alice', 'Bob', 'Charlie']
# B. Tuple

# A tuple with fixed types in order.

from typing import Tuple

student: Tuple[str, int] = ("Alice", 22)

print(student)

# Output

# ('Alice', 22)

# # Step-by-Step

# # Index 0

# # ↓

# # String

# # ↓

# # Alice

# # Index 1

# # ↓

# # Integer

# # ↓

# # 22
# # C. Dictionary
from typing import Dict

marks: Dict[str, int] = {
    "Alice": 90,
    "Bob": 80
}

print(marks)

# Output

# {'Alice': 90, 'Bob': 80}

# Meaning

# Key

# ↓

# String

# Value

# ↓

# Integer
# D. Union

# A variable can hold more than one type.

from typing import Union

id: Union[int, str]

id = 101

print(id)

id = "EMP101"

print(id)

# Output

# 101
# EMP101

# Meaning

# Union[int, str]

# ↓

# Can store Integer

# OR

# String


# | Topic              | Purpose                                        | Example                          |
# | ------------------ | ---------------------------------------------- | -------------------------------- |
# | Walrus (`:=`)      | Assign and use a value in one expression       | `(n := len(list)) > 3`           |
# | Type Hint          | Specify expected data type                     | `age: int = 25`                  |
# | Function Type Hint | Specify parameter and return types             | `def add(a: int, b: int) -> int` |
# | `List[int]`        | List containing integers                       | `[1, 2, 3]`                      |
# | `Tuple[str, int]`  | Fixed sequence of different types              | `("Alice", 20)`                  |
# | `Dict[str, int]`   | Dictionary with string keys and integer values | `{"Alice": 90}`                  |
# | `Union[int, str]`  | Variable can hold multiple types               | `101` or `"EMP101"`              |

# Benefits of Type Hints
# | Benefit               | Explanation                                               |
# | --------------------- | --------------------------------------------------------- |
# | Better readability    | You immediately know expected data types.                 |
# | Easier maintenance    | You understand old code quickly.                          |
# | IDE support           | Better autocomplete and warnings.                         |
# | Fewer bugs            | Many type mistakes are caught before running the program. |
# | Better teamwork       | Other developers know how to use your functions.          |
# | Self-documenting code | The function signature explains itself.                   |

# Interview Answer (2–3 lines)

# Why do we use type hints in Python?

# Type hints improve code readability and maintainability by showing the expected data types of variables, 
# function parameters, and return values. 
# They help IDEs and static type checkers detect type-related mistakes early, although Python does not enforce them at runtime.