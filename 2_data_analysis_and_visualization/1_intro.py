"""
Data analysis is the systematic process of examining raw data to uncover hidden patterns, trends, and relationships. It involves a series of steps, including collecting, cleaning, transforming, and modeling data, ultimately aimed at answering critical questions, solving complex problems, and facilitating informed decision-making.

dataset:
Time-series datasets: The chronicles of change(track changes over time)
        Financial data providers like Yahoo Finance, Quandl, and Alpha Vantage
        U.S. Census Bureau, the Bureau of Labor Statistics, and the National Oceanic and Atmospheric Administration (NOAA), provide access to a plethora of time-series datasets related to demographics, economics, and the environment
        Kaggle and Data.gov

Cross-sectional datasets: A snapshot in time(a snapshot of the relationships between various variables at a particular instant.)
        characteristics of different individuals or groups at a single moment, constitutes a cross-sectional dataset
        Provider :  Inter-university Consortium for Political and Social Research (ICPSR) or data published by research organizations such as Pew Research Center.

Panel datasets: The longitudinal lens
        - dataset, which follows the same individuals or entities over multiple time periods, is known as a panel dataset or longitudinal dataset. It combines the temporal dimension of time-series data with the cross-sectional perspective, offering a unique lens to study how individuals or entities change over time and how various factors influence these changes.

microsoft azure open dataset
microsoft research data repo
Microsoft Planetary Computer specializes
"""

"""
tools in pandas
The replace() function allows you to systematically replace specific values or patterns in your data, ensuring uniformity. 
 apply() function provides flexibility to apply custom functions to your data, enabling you to tailor your cleaning process to specific needs. 
use regular expressions to enforce consistent formatting of names, addresses, or other textual data.
use data dictionaries or metadata to define valid values and ranges for different variables, ensuring data integrity and consistency.
"""

# pandas -> data cleaning and preparation library
import pandas as pd

# Sample data
data = {
    "age": [25, 30, 35, 40],
    "gender": ["male", "female", "male", "female"],
    "income": [50000, 60000, 75000, 55000],
}

# Create a DataFrame
df = pd.DataFrame(data)
print(df.head())
print(df.info())
print(df.describe())

# Convert 'gender' to a categorical variable
df["gender"] = df["gender"].astype("category")

# Calculate average income
average_income = df["income"].mean()

# Count the number of males and females
gender_counts = df["gender"].value_counts()

print(average_income)
print(gender_counts)
