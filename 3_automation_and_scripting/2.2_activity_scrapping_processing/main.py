# Step 3.1: Fetch HTML Content
# Please be careful to follow instructions on how to run the program;
# the Run menu or right-click > Run options do not work in the simulated environment.
# Ensure you have run the terminal command to install the correct libraries using pip.
# You must use the terminal window as directed in Step 3.
### YOUR CODE HERE ###
import requests
from bs4 import BeautifulSoup

# Fetch the webpage content
url = "http://127.0.0.1:5500/3_automation_and_scripting/2.2_activity_scrapping_processing/baseball_stats.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Print the HTML content to inspect
print(soup.prettify())


# Step 3.2: Extract the Required Data
### YOUR CODE HERE ###
table = soup.find("table")
# extract headers
headers = [th.get_text(strip=True) for th in table.findAll("th")]
# extract table rows
rows = table.find("tbody").find_all("tr")
games_data = []
for row in rows:
    cells = [td.get_text(strip=True) for td in row.find_all("td")]
    game_dict = dict(zip(headers, cells))
    games_data.append(game_dict)

print(games_data)

# Step 4.1: Convert to a DataFrame
# Import pandas
### YOUR CODE HERE ###
import pandas as pd

# Convert the game data into a pandas DataFrame
### YOUR CODE HERE ###
df = pd.DataFrame(games_data)


# Inspect the DataFrame
### YOUR CODE HERE ###
print("df: ", df)

# Save and print the shaped data
### YOUR CODE HERE ###
print("DataFrame shape:", df.shape)

# Step 5.1: Save to a CSV File
# Save the DataFrame to a CSV file named sports_statistics.csv
### YOUR CODE HERE ###
df.to_csv("sports_statistics.csv", index=False)
