from bs4 import BeautifulSoup

# Sample HTML content
html_content = """
<html>
<body>
    <h1>This is a heading</h1>
    <p>This is a paragraph.</p>
    <p class="special">This is another paragraph.</p>
</body>
</html>
"""

# Parse the HTML
soup = BeautifulSoup(html_content, "html.parser")
print(soup)

# Find the first 'p' element
first_paragraph = soup.find("p")
print(first_paragraph)  # Output: <p>This is a paragraph.</p>

# Find all 'p' elements
all_paragraphs = soup.find_all("p")
for paragraph in all_paragraphs:
    print(paragraph)

# Find the 'p' element with the class 'special'
special_paragraph = soup.find("p", class_="special")
print(special_paragraph)  # Output: <p class="special">This is another paragraph.</p>


html_content = """
<html>
<body>
    <div id="main-content">
        <h1>This is a heading</h1>
        <p class="important">This is an important paragraph.</p>
        <a href="https://www.example.com">Visit Example</a>
    </div>
</body>
</html>
"""

# Parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Use CSS selector to find the 'div' with id 'main-content'
main_content = soup.select_one("#main-content")

# Find the 'p' element with class 'important' within 'main-content'
important_paragraph = main_content.select_one(".important")

# Extract the text content of the paragraph
paragraph_text = important_paragraph.get_text()
print(paragraph_text)  # Output: This is an important paragraph.

# Find the 'a' element within 'main-content'
link = main_content.select_one("a")

# Access the 'href' attribute of the link
link_url = link["href"]
print(link_url)  # Output: https://www.example.com


html_content = """
<div class="product">
  <h1>Awesome Headphones</h1>
  <p class="price">$99.99</p>
  <p class="description">These headphones offer amazing sound quality!</p>
</div>
"""

soup = BeautifulSoup(html_content, "html.parser")

# Use soup.find() to locate the <h1> tag and store the extracted text in a variable called 'product_name'.
### YOUR CODE HERE ###
product_name = soup.find("h1").get_text()

# Use soup.find() to locate <p> tags with class_='price' and store the extracted text in a variable called 'price'.
### YOUR CODE HERE ###
price = soup.find("p", class_="price").get_text()

# Use soup.find() to locate <p> tags with class_='description' and store the extracted text in a variable called 'description'.
### YOUR CODE HERE ###
description = soup.find("p", class_="description").get_text()

# Print the extracted data in the format:
print(f"Product name: {product_name}")
print(f"Price: {price}")
print(f"Description: {description}")
