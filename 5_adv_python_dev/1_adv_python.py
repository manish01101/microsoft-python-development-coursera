"""
Decorators: Enhancing functionality with a touch of magic
Decorators are essentially functions that take another function as input and return a new function with enhanced functionality. They act as wrappers, allowing you to add new features or modify the behavior of existing functions without altering their core logic.
types of decorators:
- function decorators
- class decorators
- method decorators

Generators: Generating values on demand
The core of a generator's functionality lies in the `yield` keyword. When a generator function encounters a yield statement, it pauses its execution and returns the specified value. The function's state is preserved, allowing it to resume exactly where it left off the next time it's called. This ability to suspend and resume execution is what enables generators to generate values on the fly.

Context managers: Managing resources with grace
Context managers are defined using the with statement in Python. This statement creates a temporary context within which the resource is acquired and used. The key advantage of the with statement is that it guarantees the proper release of the resource, even if exceptions occur during the code's execution. This ensures that resources are not left dangling and prevents potential memory leaks or other resource-related issues.
"""

# decorator
from functools import lru_cache


@lru_cache(maxsize=None)
def fibonacci(n):
    """Calculates the nth Fibonacci number."""

    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Calculate the 35th Fibonacci number
print(fibonacci(35))


import logging


def logger(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned: {result}")
        return result

    return wrapper


"""A decorator that logs function calls."""
logging.basicConfig(filename="my_app.log", level=logging.INFO)


@logger
def my_function(a, b):
    """A simple function that adds two numbers."""
    return a + b


result = my_function(5, 3)
print(f"Result: {result}")
