import matplotlib.pyplot as plt

# Create a figure with a specific size
# fig = plt.figure(figsize=(10, 6))  # Width: 10 inches, Height: 6 inches

"""
Within the figure, the axes are where the actual plotting takes place. Imagine the axes as a graph paper grid laid on your canvas, providing the framework for organizing and displaying your data. It's here that you'll plot your data points, lines, bars, or any other visual representation. You can have multiple axes within a single figure, enabling you to create subplots or side-by-side comparisons. Each set of axes functions as an independent plotting area, allowing you to visualize different aspects of your data or compare multiple datasets within the same figure.

"""

# Create a figure with 2 rows and 2 columns of subplots
fig, ax = plt.subplots(2, 2)

# Access individual subplots using indexing
ax[0, 0].plot([1, 2, 3], [4, 5, 6])  # Top-left subplot
ax[0, 1].bar(["A", "B", "C"], [7, 8, 9])  # Top-right subplot
ax[1, 0].scatter([10, 20, 30], [11, 12, 13])  # Bottom-left subplot
ax[1, 1].hist([1, 1, 2, 3, 3, 3])  # Bottom-right subplot

plt.show()

x = [1, 2, 3]
y = [4, 5, 6]

plt.plot(x, y)
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")
plt.title("Plot Title")
plt.show()

# Ticks and tick labels
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)

# Set tick locations and labels for the x-axis
plt.xticks(np.arange(0, 11, 2), ["0", "2", "4", "6", "8", "10"])

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

plt.show()


"""
LEGENDS: decoding the different symbols, colors, or line styles used to represent each element in your plot.
"""
x = [1, 2, 3]
y1 = [4, 5, 6]
y2 = [7, 8, 9]

plt.plot(x, y1, label="Data Series 1")
plt.plot(x, y2, label="Data Series 2")

plt.legend()  # Automatically creates a legend based on labels
plt.show()


# Simple line plots: Unveiling trends and patterns
x = np.linspace(0, 10, 100)  # Generate 100 evenly spaced points from 0 to 10
y = np.sin(x)  # Compute the sine of each x value

plt.plot(x, y)
plt.xlabel("Time (days)")  # Label the x-axis
plt.ylabel("Stock Price ($)")  # Label the y-axis
plt.title("Stock Price Trend")  # Add a title
plt.show()  # Display the plot


# Scatter plots: Unveiling relationships and correlations
ages = np.linspace(20, 60, 100)  # Ages ranging from 20 to 60
income = ages * 500 + np.random.normal(
    0, 10000, 100
)  # Simulating a positive correlation with some noise

plt.scatter(ages, income)
plt.xlabel("Age")
plt.ylabel("Income")
plt.title("Age vs. Income")
plt.show()


# Bar charts: Comparing values across categories
categories = ["Product A", "Product B", "Product C", "Product D"]
values = [1500, 2300, 1200, 3000]

plt.bar(categories, values)
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Product Sales Comparison")
plt.show()


# Histograms: Visualizing data distribution
data = np.random.randn(
    1000
)  # Generate 1000 random numbers from a standard normal distribution

plt.hist(data, bins=30)  # Create a histogram with 30 bins
plt.xlabel("Exam Score")
plt.ylabel("Number of Students")
plt.title("Distribution of Exam Scores")
plt.show()


# Pie charts: Showcasing proportions and percentages
labels = ["Windows", "macOS", "Linux", "Other"]
sizes = [70, 20, 5, 5]

plt.pie(sizes, labels=labels, autopct="%1.1f%%")  # Display percentages on each slice
plt.title("Market Share of Operating Systems")
plt.show()

"""
Colors: Fine-tune the colors of your plots to enhance visual appeal and clarity.
Markers: Choose from a variety of markers to represent data points in scatter plots and line plots.
Line styles: Customize the appearance of lines in your plots with different styles (e.g., solid, dashed, dotted).
Legends: Add clear and informative legends to explain the elements within your visualizations.
Annotations: Include text annotations to highlight specific data points or regions of interest.

advanced plotting techniques:
3D plotting: Create visualizations in three dimensions to represent complex data relationships.
Animation: Generate dynamic visualizations that evolve over time to illustrate changes or trends.3
Interactive plots: Develop interactive plots that respond to user input, allowing for deeper exploration of the data.


visualization library:
- matplotlib
- apache superset
- plotly: Plotly lets you build interactive charts and graphs that work in web browsers
- bokeh: Bokeh is great for making interactive charts and graphs that work well in websites and apps
"""
