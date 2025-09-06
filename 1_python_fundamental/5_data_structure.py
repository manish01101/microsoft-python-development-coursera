# List
my_list = [1, 2.1, "hello", [3, 4]] # mutable
my_list[1:3]
print(my_list[1:3])
my_list.extend([5, 6])
my_list.append(7)
my_list.insert(0, 0)
my_list.remove(2.1)
my_list.pop()
print(my_list)
# my_list.sort()  # This will raise an error because the list contains mixed types
my_list.reverse()
print(my_list)
len(my_list)
my_list.count(1)
my_list.index("hello")
my_list.clear()
my_list.copy()


# Tuple
my_tuple = (10, 20, "python") # immutable
print("tuple is: ", my_tuple)

# set (a special type of set called "frozenset" that is immutable)
my_set = {1, 2, 3, 3} # mutable, unordered, no duplicates
print("set is: ", my_set)
my_set.add(4)
my_set.remove(2)
print("set is: ", my_set)
my_set.discard(5)  # does not raise an error if the element is not found
my_set.pop()  # removes and returns an arbitrary element
my_set.clear()
my_set.copy() # shallow copy  

# Dictionary
my_dict = {"name": "Alice", "age": 30, "city": "New York"} #Mutability and flexibility
print("dictionary is: ", my_dict)
my_dict["age"] = 31  # update value
my_dict["job"] = "Engineer"  # add new key-value pair
print("dictionary is: ", my_dict)

# example
# Add the SKU data provided to the product catalog dictionary
product_catalog = {} 
product_catalog["SKU123"] = {
    "name": "Widget A",
    "price": 19.99,
    "quantity": 50
}
product_catalog["SKU456"] = {
    "name": "Widget B",
    "price": 34.95,
    "quantity": 25
}
product_catalog["SKU789"] = {
    "name": "Widget C",
    "price": 9.99,
    "quantity": 100
}

# Look up this SKU in your code. 
sku_to_find = "SKU123"
price = product_catalog["SKU123"]["price"]
print(f"The price of {product_catalog[sku_to_find]['name']} is ${price}")


# Coding example: Comparing list and dictionary lookup
import timeit

# List lookup
list_data = list(range(100000))
lookup_value = 99999
list_time = timeit.timeit(lambda: lookup_value in list_data, number=1000)

# Dictionary lookup
dict_data = {i: i for i in range(100000)}
dict_time = timeit.timeit(lambda: lookup_value in dict_data, number=1000)

print("List lookup time:", list_time)
print("Dictionary lookup time:", dict_time)





'''
Alternative structures:

Python also offers more specialized structures like deque (for efficient appends/pops at both ends), heapq (for priority queues), and collections.Counter (for counting occurrences)
'''
from collections import deque, Counter

# Deque example
queue = deque()
queue.append("task1")
queue.append("task2")
print(queue.popleft())  # Output: task1

# Counter example
text = "This is a sample text with some repeated words words"
word_counts = Counter(text.split())
print(word_counts)  # Output: Counter({'words': 2, 'This': 1, 'is': 1, ...})