"""
Docstring for 4_webdev_python.2_python_web_framework

Django key attributes:
- comprehensive approach (provide built-in tools and features)
- mvt architecture
- open-source philosophy

MVT - model view template
model defines the structure of the data
view handles the business logic
template manages the presentation layer

example: for an ecommerce site, models defines products, customers, and orders, view handles task like displaying product lists and customer profiles, while templates control how this info is presented to the user, such as styling a product page or formatting and order confirmation.

Flask key attributes:
- minimalist approach
- open-source philosophy
- extension support


Django vs Flask

Django is a batteries-included Python web framework that provides most of the tools needed for web development out of the box. It follows the Model-View-Template (MVT) architecture and includes a powerful ORM, an auto-generated admin interface, and strong built-in security features like protection against XSS, CSRF, and SQL injection. Django is designed for scalability and maintainability, making it ideal for large-scale applications such as CMS platforms, e-commerce sites, enterprise systems, and social networking applications. While its extensive feature set can feel overwhelming at first, its structured approach and rich documentation help streamline development for complex projects.

Flask, on the other hand, is a lightweight microframework that focuses on simplicity and flexibility. It provides a minimal core and allows developers to choose only the components they need through extensions. Flask is easy to learn, quick to set up, and gives developers full control over project structure and dependencies. Its lightweight nature often results in better performance for smaller applications. Flask is best suited for small to medium projects, REST APIs, prototyping, and microservices, where flexibility and speed of development are more important than built-in features.

Downsides
- Django's all-in-one approach can feel complex for beginners and may add unnecessary overhead for small projects.
- Flask's flexibility requires more upfront architectural decisions, which can be challenging without experience.

Final takeaway
Choose Django for large, complex, and feature-rich applications where structure, security, and scalability matter.
Choose Flask for simple apps, APIs, prototypes, or microservices where flexibility, performance, and minimalism are key.


In Flask, you define routes using decorators, which are special functions that modify the behavior of other functions. These decorators associate specific URL endpoints with corresponding Python functions, known as view functions. When a user accesses a particular URL, Flask consults its routing table and identifies the associated view function, which then executes and generates the content that the user sees in their web browser.

Gzip Compression on your web pages and assets before sending them to the client can significantly reduce the amount of data transferred, leading to faster page loads.



How Flask uses templating
Flask uses templates to separate application logic (Python) from presentation (HTML).

Instead of writing HTML directly inside your Python code, Flask:
1. Handles logic in routes (Python functions)
2. Passes data to HTML templates
3. Renders dynamic content for the user

Flask uses Jinja2 as its templating engine by default.

Basic flow in Flask templating
1. User requests a URL (e.g. `/`)
2. Flask route runs Python logic
3. Flask sends data to a template using `render_template()`
4. Jinja2 combines HTML + data
5. Final HTML is sent to the browser

Example

app.py

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    username = "Manish"
    return render_template('index.html', name=username)
```

templates/index.html

```html
<!DOCTYPE html>
<html>
<body>
    <h1>Hello, {{ name }}!</h1>
</body>
</html>
```

Output in browser:

```
Hello, Manish!
```

What is the primary purpose of a templating engine like Jinja2?
The main purpose of Jinja2 is to:
Generate dynamic HTML by embedding Python-like logic inside HTML templates

In simple words:
* HTML stays clean and readable
* Python logic stays in Flask routes
* Jinja2 connects the two

What Jinja2 allows you to do

1. Insert dynamic data
```html
<p>Welcome, {{ user_name }}</p>
```
2. Use control structures (logic in HTML)

If condition

```html
{% if is_logged_in %}
  <p>Welcome back!</p>
{% else %}
  <p>Please log in</p>
{% endif %}
```

Loop

```html
<ul>
{% for item in items %}
  <li>{{ item }}</li>
{% endfor %}
</ul>
```

3. Reuse layouts (template inheritance)

base.html

```html
<html>
<body>
  {% block content %}{% endblock %}
</body>
</html>
```

index.html

```html
{% extends "base.html" %}

{% block content %}
  <h1>Home Page</h1>
{% endblock %}
```

This keeps large apps clean and maintainable.

Why Flask + Jinja2 is powerful
| Feature                | Benefit                          |
| ---------------------- | -------------------------------- |
| Separation of concerns | Cleaner, maintainable code       |
| Dynamic content        | Personalized pages               |
| Reusable templates     | Less duplication                 |
| Built-in security      | Auto-escapes HTML (prevents XSS) |
| Easy syntax            | Beginner-friendly                |

NOTE: Flask uses Jinja2 templates to separate business logic from presentation, allowing dynamic HTML generation using variables, loops, and conditionals.

"""
