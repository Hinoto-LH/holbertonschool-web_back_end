# Python Variable Annotations

## Type Annotations in Python 3

Type annotations (introduced in Python 3.5 via [PEP 484](https://peps.python.org/pep-0484/)) allow you to explicitly declare the expected types of variables, function parameters, and return values. They are purely **optional** and do not affect runtime behavior — Python remains dynamically typed.

---

## Annotating Variables

```python
name: str = "Alice"
age: int = 30
pi: float = 3.14
is_active: bool = True
```

You can also annotate without assigning a value:

```python
count: int
```

---

## Annotating Function Signatures

Annotate parameters and return types directly in the function definition:

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

def nothing() -> None:
    print("No return value")
```

### Complex Types

Use the `typing` module for more complex type hints:

```python
from typing import List, Dict, Tuple, Optional, Union

def get_names() -> List[str]:
    return ["Alice", "Bob"]

def get_scores() -> Dict[str, int]:
    return {"Alice": 95, "Bob": 87}

def first_and_last(items: List[int]) -> Tuple[int, int]:
    return items[0], items[-1]

# Optional means the value can be the type OR None
def find_user(user_id: int) -> Optional[str]:
    return None

# Union means the value can be one of several types
def process(value: Union[int, str]) -> str:
    return str(value)
```

From Python 3.10+, you can use the `|` operator instead of `Union`:

```python
def process(value: int | str) -> str:
    return str(value)
```

---

## Duck Typing

Python follows the principle of **duck typing**:

> "If it walks like a duck and quacks like a duck, then it's a duck."

This means Python cares about **what an object can do** (its methods and attributes), not **what it is** (its type).

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def make_it_speak(animal):
    print(animal.speak())  # Works for any object with a .speak() method

make_it_speak(Dog())  # Woof!
make_it_speak(Cat())  # Meow!
```

### Duck Typing with Type Annotations

The `typing` module provides `Protocol` (Python 3.8+) to formally describe duck typing contracts:

```python
from typing import Protocol

class Speakable(Protocol):
    def speak(self) -> str:
        ...

def make_it_speak(animal: Speakable) -> None:
    print(animal.speak())
```

Any class that implements `speak()` is implicitly compatible — no explicit inheritance needed.

---

## Validating Your Code with mypy

[mypy](https://mypy.readthedocs.io/) is a static type checker for Python. It reads your type annotations and reports type errors **before you run your code**.

### Installation

```bash
pip install mypy
```

### Basic Usage

```bash
mypy my_file.py
```

### Example

Given this file `example.py`:

```python
def add(a: int, b: int) -> int:
    return a + b

result: str = add(1, 2)  # Type error: int assigned to str
```

Running `mypy example.py` outputs:

```
example.py:4: error: Incompatible types in assignment (expression has type "int", variable has type "str")
Found 1 error in 1 file (checked 1 source file)
```

### Useful mypy Flags

| Flag | Description |
|------|-------------|
| `--strict` | Enable all optional checks |
| `--ignore-missing-imports` | Suppress errors for missing stubs |
| `--disallow-untyped-defs` | Require all functions to be annotated |
| `--check-untyped-defs` | Type-check the body of unannotated functions |

```bash
mypy --strict my_file.py
```

### Checking an Entire Project

```bash
mypy .
```

---

## Summary

| Concept | Description |
|---------|-------------|
| Type annotations | Hints that declare expected types for variables and functions |
| `typing` module | Provides `List`, `Dict`, `Optional`, `Union`, `Protocol`, etc. |
| Duck typing | Objects are compatible if they have the required methods/attributes |
| `mypy` | Static analysis tool that validates type annotations without running code |
