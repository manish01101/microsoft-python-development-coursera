"""
automation tools & lib
task scheduler (windows)
crontab (unix)
Selenium is a game-changer for web automation, empowering you to scrape data, test web applications, and automate repetitive browser tasks.
beautifulsoup for parsing web pages,
Requests for making HTTP requests,
Schedule for simple task scheduling, and
PyAutoGUI for controlling your mouse and keyboard programmatically.

10 questions to ask before automating a task
1. How frequently is the task performed?
2. How complex is the task?
3. What's the potential Return on Investment (ROI)?
4. How prone to errors is the manual process?
5. Does the task require human interaction or decision-making?
6. Is the task standardized and predictable?
7. Are the necessary data and resources available?
8. What are the potential risks and downfalls?
9. How will automation impact employees?
10. Is the technology available and mature enough?

"""

# Generate an automation workflow for data collection from csv and website
import pandas as pd
import requests
from bs4 import BeautifulSoup


def extract_from_website(url):
    # Function to extract data from html website
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Find a table element
        table = soup.find("table")

        # If a table is found, extract the data
        if table:
            headers = [th.text for th in table.find("tr").find_all("th")]
            data = []
            # The loop will find all tr tags (table rows)
            for row in table.find_all("tr")[1:]:
                # Within each table row, select all td (table data)
                row_data = [td.text for td in row.find_all("td")]
                # Appends the value from the td to the data array
                data.append(dict(zip(headers, row_data)))

            return pd.DataFrame(data)
        else:
            print("No table found on the page.")
            return None
    except Exception as e:
        print(f"Error fetching URL: {e}")
        return None


def gather_data_from_sources():
    data_from_csv = pd.read_csv("sales_data.csv")
    # Example: Fetching data from a website using requests & BeautifulSoup
    web_data_url = "https://example.com/marketing_data"
    data_from_website = extract_from_website(web_data_url)
    return pd.concat([data_from_csv, data_from_website], axis=1)  # Combine data


def process_and_format_data(data):
    # ... Process data to create Price Per Unit column.
    formatted_data = data[["Total Order Price", "Number of Units"]]
    formatted_data["Price Per Unit"] = (
        formatted_data["Total Order Price"] / formatted_data["Number of Units"]
    )
    return formatted_data


def generate_report(data):
    # Generate final report (could use pandas' to_excel, or libraries like ReportLab, matplotlib, etc).
    data.to_excel("marketing_report.xlsx")
    print("Report generated successfully!")


# Main Automation Flow
raw_data = gather_data_from_sources()
processed_data = process_and_format_data(raw_data)
generate_report(processed_data)

"""
The argparse library is the go-to solution for handling command-line arguments in Python. 
"""
import argparse

parser = argparse.ArgumentParser(description="A friendly greeting script.")
parser.add_argument("name", help="The name of the person to greet.")
args = parser.parse_args()
print(f"Hello, {args.name}!")

"""
the sys.argv list stands out as a crucial element for interacting with command-line arguments.
"""
import sys

if len(sys.argv) > 1:
    name = sys.argv[1]
    print(f"Hello, {name}!")
else:
    print("Hello, there!")


"""
Data piping
One of the most powerful features enabled by the subprocess module is the ability to pipe data between commands.
"""
# Python error_finder.py
import subprocess

# Use grep to find lines containing "error" in a log file
grep_process = subprocess.Popen(
    ["grep", "error", "logfile.txt"], stdout=subprocess.PIPE
)

# Pass the output of grep to a Python script for further analysis
python_process = subprocess.Popen(
    ["python", "analyze_errors.py"], stdin=grep_process.stdout
)

# Wait for the Python script to finish
python_process.wait()


# Python analyze_errors.py
import sys

# Read lines containing "error" from standard input (provided by subprocess)
for line in sys.stdin:
    # Process each error line
    print(f"Found: {line.strip()}")

print("Finished analyzing errors.")

"""
Batch processing
"""
import os
import subprocess

for filename in os.listdir("data_directory"):
    if filename.endswith(".csv"):
        # Convert CSV files to Excel using a shell command
        subprocess.call(["libreoffice", "--convert-to", "xls", filename])

"""
Error handling and robustness
"""
import subprocess

try:
    subprocess.run(
        ["rm", "important_file.txt"], check=True
    )  # Delete a file, raise an error if it fails
except subprocess.CalledProcessError as e:
    print(f"Error deleting file: {e}")
