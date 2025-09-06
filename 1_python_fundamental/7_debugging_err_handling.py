'''
Debugging is the detective work of programming. It's about systematically investigating your code to find and fix those hidden bugs, errors or flaws in the code that cause it to behave incorrectly. Debugging is the process of tracking down and eliminating these bugs.

1. try/except → Handling errors
You use try/except when you want to catch and handle an exception (instead of letting the program crash).
try:
    x = 10 / 0   # ZeroDivisionError
except ZeroDivisionError as e:
    print("You cannot divide by zero:", e)
output: You cannot divide by zero: division by zero

2. raise → Creating / re-throwing errors
You use raise when you want to manually trigger an exception.
This is useful if you want to enforce conditions, validate inputs, or re-raise an error after catching it.

def divide(a, b):
    if b == 0:
        raise ValueError("Denominator cannot be zero")
    return a / b

print(divide(10, 2))  # ✅ Works
print(divide(10, 0))  # ❌ Raises ValueError

output: 5.0
Traceback (most recent call last):
  ...
ValueError: Denominator cannot be zero

🔹 3. Using both together
Sometimes you try/except to catch an error, but still raise it again (for logging, debugging, or re-throwing to a higher level):

try:
    x = int("abc")  # ValueError
except ValueError as e:
    print("Logging error:", e)
    raise   # re-raises the same error

output: Logging error: invalid literal for int() with base 10: 'abc'
Traceback (most recent call last):
  ...
ValueError: invalid literal for int() with base 10: 'abc'

✅ Summary
try/except → Catch & handle errors gracefully.
raise → Generate an error (or re-throw one).
'''
import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG)
logging.debug('This is a debug message')
logging.info('This is an informational   message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')  

'''
Logging offers several advantages over simple print statements:
Log messages are saved, allowing you to review them later, even after the program has finished running.
You can structure log messages with timestamps, module names, and other relevant details, making it easier to pinpoint issues.
You can adjust logging levels to control the amount of information logged, focusing on relevant details.
Logging is particularly valuable for long-running applications, complex systems, and scenarios where you need to track events over time.

logging for long-term monitoring, debuggers for real-time inspection, print statements for quick checks, and online resources for expert guidance
'''

# assertion
def calculate_area(length, width):
    assert length > 0, "Length must be positive"
    assert width > 0, "Width must be positive"
    return length * width

print(calculate_area(-1, 3))

file_name = "sample.txt"
try:
    with open(file_name, 'r') as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print("Error: File not found -", file_name)


import logging
logging.basicConfig(filename='app.log', level=logging.DEBUG)
def divide(x, y):
    try:
        result = x / y
        logging.info(f"Successfully divided {x} by {y} to get {result}")
        return result
    except ZeroDivisionError:
        logging.error("Division by zero attempted!")
        return None
divide(10, 2)
divide(5, 0)