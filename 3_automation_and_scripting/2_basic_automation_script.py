"""
The os module
os.mkdir()
os.rmdir()
os.mknod() -> create empty files
os.remove() -> delete files
os.rename()
os.getcwd() -> current working directory
os.chdir() -> change dir
os.listdir()
os.access() -> function to verify if you have the required files permissions
os.stat() -> detailed information about a file.
| Attribute| Data Type| How to Interpret / Convert                                                                             |
| ---------| ---------| -------------------------------------------------------------------------------------------------------|
| st_size  | int      | Size of the file in bytes                                                                              |
| st_mtime | float    | Last modification time; represents seconds since the Unix epoch. Convert using datetime.fromtimestamp()|
| st_mode  | int      | File permissions and type; convert to a human-readable format (e.g., -rwxrwxrwx) using stat.filemode() |


os.path submodule helps you navigate these paths
os.path.join() -> join different parts of a path together
os.path.basename() ->  extract just the filename from a path
os.path.exists() -> check if a particular path exists


The shutil module: file management assistant.
shutil.copy() -> copy files
shutil.copytree() -> copy an entire folder and all its contents
shutil.move()
shutil.rmtree() -> removes a directory and everything inside it


glob module :=> It's like a powerful search engine for your file system, allowing you to find files and directories that match certain patterns.

glob.glob('*.txt') -> finds all files in the current directory
glob.glob('**/*.py', recursive=True) -> searches for files ending in .txt not only in the current directory but also in all its subdirectories.
glob.glob('*.[txt,pdf]') -> square brackets define a set of possible matches.
glob.glob('data/202*/sales_*.csv') -> searches the "data" directory for files starting with "sales_" and ending with ".csv" within any subdirectories that start with 202 (so, 2024 or 2025, or even 2026-preview).

"""

"""----search file-----"""
import glob

pdf_files = glob.glob("./**/*.pdf", recursive=True)
print(pdf_files)

pdf_files = glob.glob("*.pdf")
for pdf_file in pdf_files:
    print(pdf_file)

"""---rename file----"""
import os

for i in range(1, 11):
    old_name = f"IMG_{i:03d}.jpg"
    new_name = f"vacation_photo_{i}.jpg"
    os.rename(old_name, new_name)

import glob

files = glob.glob("*.*")
for file in files:
    os.stat(file)
    os.mkdir()

# Opening and reading a file
file = open("input.txt", "r")
content = file.read()
print(content)
file.close()

# Using with statement to open and read a file: automatically closes the file once the block is exited
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Appending to a text file
with open("newfile.txt", "a") as file:
    file.write("Adding a new line to the existing file.\n")


# Reading a CSV file
import csv

with open("example.csv", mode="r") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)

"""
-----reg expr-----
\d+ -> matches one or more digits (0-9)
[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,} -> email
\b\w+\b -> matches individual words.
\d{3}-\d{3}-\d{4}  -> matches phone numbers 
https?://[^\s]+  -> matches URLs
`r"\b\d{1,2}[-/]\d{1,2}[-/]\d{2,4}\b"` -> Dates
"""
import re

# Save the pattern in a variable for comparison
phone_number_pattern = r"^(\d{3}) \d{3}-\d{4}$"
user_input = input("enter: ")
# Compare the user_input variable to the regex pattern
if re.match(phone_number_pattern, user_input):
    print(f"{user_input} is a valid phone number.")
else:
    print(f"{user_input} is not a valid phone number.")


# Removing duplicates
import pandas as pd

# Sample data with duplicate rows
data = {
    "name": ["Alice", "Bob", "Charlie", "Alice", "David"],
    "age": [25, 30, 35, 25, 40],
}
df = pd.DataFrame(data)

# Identify duplicate rows
duplicates = df.duplicated()
print("Duplicate rows:\n", duplicates)

# Remove duplicate rows
df_cleaned = df.drop_duplicates()
print("\nCleaned DataFrame:\n", df_cleaned)


# Fixing inconsistent data
import pandas as pd

# Sample data with inconsistent date formats
data = {
    "date": ["2023-12-31", "12/30/2023", "2023-01-01", "01/02/2023"],
    "category": ["Electronics", "electronics", "ELECTRONICS", "Electronic"],
}
df = pd.DataFrame(data)

# Standardize date formats
# df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d", errors="coerce")
df["date"] = pd.to_datetime(df["date"], format="%m/%d/%Y", errors="coerce")
df["date"] = df["date"].fillna(pd.to_datetime(df["date"], format="%Y-%m-%d"))

# Standardize categorical values
df["category"] = df["category"].str.lower()
print(df)


# Filling missing prices
import pandas as pd
import numpy as np

# Create a DataFrame with missing values
data = {"price": [100, 150, np.nan, 200, np.nan, 180, 120]}
df = pd.DataFrame(data)

# Print the DataFrame before filling missing values
print("Before filling missing values:")
print(df)

# Fill missing values with the median
### YOUR CODE HERE ###
df_median = df["price"].median()
df["price"].fillna(df_median, inplace=True)
# Print the DataFrame after filling missing values
print("\nAfter filling missing values:")
print(df)


""" regular expressions
. (dot): Matches any single character except a newline.
* (asterisk): Matches zero or more occurrences of the preceding element.
+ (plus): Matches one or more occurrences of the preceding element.
? (question mark): Matches zero or one occurrence of the preceding element.
[] (character class): Matches any single character within the brackets. For example, [aeiou] matches any vowel.
^ (caret): When used inside a character class, it negates the class. For example, [^aeiou] matches any character that is not a vowel.
{} to specify a more precise range. For example, a{2,4} matches "aa", "aaa", or "aaaa".
Anchors: Anchors match the start (^) or end ($) of a string.
"""
import re

text = "Please contact me at john.doe@example.com or jane.doe@company.org for more information."
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
email_matches = re.findall(email_pattern, text)
print(email_matches)
