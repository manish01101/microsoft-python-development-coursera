"""
Dataframe consists of 3 components: data, index, column
common operation: indexing, slicing, filtering
indexing:access specific elements within a DataFrame, indexing by row labels using the function.lock accessor, or by integer position using the function.ilock accessor.
slicing:to select a range of rows or columns at once

Two of the most fundamental indexing methods in pandas are .loc and .iloc
.loc method is label-based, meaning it uses row and column labels to access data
.iloc is position-based, .iloc is useful when you need to access data based on its position within the DataFrame, regardless of the labels

Boolean indexing, also known as mask-based indexing, is like having a powerful filter for your DataFrame. You create a boolean mask, which is essentially an array of True and False values that indicate which rows or columns meet specific criteria.
find all customers who are 'Platinum' members and have made more than 10 purchases
->  df[(df['membership_level'] == 'Platinum') & (df['number_of_purchases'] > 10)]

.at is label-based, while .iat is integer-based.
Multi-level indexing (hierarchical indexing) can be used when your data has a natural hierarchy
query() Method offers a SQL-like syntax for querying DataFrames
Handle missing data: Use methods like .fillna() or .dropna() to handle them

df.dropna() removes rows containing any missing value
df.fillna(0) replaces missing values with a specified value (e.g., 0)
df['Age'].fillna(df['Age'].mean(), inplace=True) is a more sophisticated approach, imputing missing values in a column with its mean. The inplace=True argument modifies the DataFrame directly, conserving memory
"""

import pandas as pd

df = pd.read_csv("salesdata.csv")
df.head()
df_sorted = df.sort_values(by="sales", ascending=False)
df_grouped = df.groupby("region")["sales"].sum()
mean_sales = df["sales"].mean()
df_filtered = df[df["sales"] > 1000]


def cal_discount(sales):
    return sales * 0.9


df["discounted_sales"] = df["sales"].apply(cal_discount)
df_pivot = df.pivot_table(index="region", columns="product", values="sales")

import numpy as np

# Sample DataFrame with missing values
data = {
    "Name": ["Alice", "Bob", np.nan, "David"],
    "Age": [25, 30, np.nan, 35],
    "City": ["New York", np.nan, "London", "Paris"],
}
df = pd.DataFrame(data)

# 1. Identifying missing values
print("Missing value counts per column:\n", df.isnull().sum())

# 2. Removing missing values (dropna)
df_dropped = df.dropna()
print("\nDataFrame after dropping rows with any missing value:\n", df_dropped)

# 3. Imputing with mean (for numerical columns)
df_filled_mean = df.fillna(df.mean(numeric_only=True))
print("\nDataFrame after filling missing 'Age' with mean:\n", df_filled_mean)

# 3. Imputing with median (for numerical columns)
df_filled_median = df.fillna(df.median(numeric_only=True))
print("\nDataFrame after filling missing 'Age' with median:\n", df_filled_median)

# 4. Handling outliers (demonstration with 'Age')
# Assuming we identify 40 as an outlier based on domain knowledge or visualization
df["Age_capped"] = df["Age"].clip(upper=40)  # Cap values at 40
print("\nDataFrame with 'Age' capped at 40:\n", df)

# 5. Data type conversion
df["Age"] = pd.to_numeric(
    df["Age"], errors="coerce"
)  # Convert to numeric, handling errors
print("\nData types after conversion:\n", df.dtypes)

# 6. Exploratory Data Analysis
print("\nDescriptive statistics:\n", df.describe())

# Group by and aggregate
grouped_data = df.groupby("City")["Age"].mean()
print("\nAverage Age by City:\n", grouped_data)


"z-scores & iqt(interquartile range) is the methods for finding outliers"
"""
Once you've identified potential outliers, you have a few options for dealing with them. First is trimming. This is the most straightforward approach. You simply remove the outliers from your data set. It's effective, but be cautious. You're losing data, which could be valuable information. Second is winsorizing. 
Instead of removing outliers, you replace them with less extreme values. For example, you might replace values above the 95th percentile with the value at the 95th percentile. This preserves more of your data while still mitigating the impact of outliers. Third is imputation. In some cases, you might choose to replace outliers with estimated values, such as the mean or median. However, use imputation with care as it can introduce bias into your analysis. The decision of how to handle outliers is not always black and white. 

"""
