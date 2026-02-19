"""
Generators are special functions in Python that produce a sequence of values on demand, instead of generating and storing them all at once. This lazy evaluation makes them incredibly memory-efficient, especially when dealing with large datasets or infinite sequences.

The yield keyword is the heart of a generator. It pauses the function's execution and returns the current line. The function's state is saved, allowing it to resume from where it left off the next time it's called.

advanced techniques-
Generator Expressions: similar to list comprehensions but use parentheses instead of brackets. For example, (x**2 for x in range(10)) generates the squares of numbers from 0 to 9.
Sending Values to Generators: can send values back into a generator using the send() method. This allows for two-way communication between the generator and the calling code, enabling more dynamic and interactive generator behavior.
Chaining Generators: You can chain multiple generators together to create complex data processing pipelines
"""


#  A generator can read and process the file line by line, yielding each line as needed, thereby minimizing memory consumption.
def log_file_reader(filename):
    """A generator that reads a log file line by line."""
    with open(filename, "r") as f:
        for line in f:
            yield line.strip()


for line in log_file_reader("my_log.txt"):
    # Process each line here
    print(line)


def fibonacci_sequence():
    """A generator that generates the Fibonacci sequence."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


# Generate the first 10 Fibonacci numbers
fib_gen = fibonacci_sequence()
for i in range(10):
    print(next(fib_gen))
