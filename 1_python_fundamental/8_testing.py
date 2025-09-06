import pytest 


'''
Test Functions:
At the core of pytest is test functions. These are plain and simple Python functions that you designate as tests by starting their names with the prefix test_.

Within these test functions, you craft assertions - statements that express your expectations about how your code should behave under specific conditions.

pytest executes these assertions, and if any of them fail, it signals a potential issue in your code that needs your attention.

A fixture is a way to set up some reusable test environment or data that your tests need.
Instead of repeating setup code in every test, you define it once as a fixture.
Fixtures can return data, objects, database connections, temporary files, etc.
You can also control their lifecycle (run before every test, once per module, once per session, etc.) with the scope parameter.

'''
def calculate_discount(price, percentage):
  return price - (price * percentage / 100)
 
class TestDiscountCalculation:
  def test_ten_percent_discount(self):
    result = calculate_discount(100, 10)
    assert result == 90  # Assertion
 
  def test_invalid_input(self):
    with pytest.raises(TypeError):
      calculate_discount("100", 10)   # Test for incorrect input typ

# Scenario 1: Web application testing - Ensuring a seamless user experience
import pytest
from your_flask_app import app  # Import your Flask app

@pytest.fixture
def client():
    """Create a test client for interacting with the Flask app."""
    app.config['TESTING'] = True  # Enable testing mode
    with app.test_client() as client:
        yield client

def test_user_registration(client):
    """Simulate a user registration and check the response."""
    data = {'username': 'testuser', 'email': 'testuser@example.com', 'password': 'testpassword'}
    response = client.post('/register', data=data)

    assert response.status_code == 302  # Expect a redirect after successful registration
    # Further checks on database or session data can be added here

def test_login(client):
    """Simulate a user login and verify the response."""
    data = {'username': 'existinguser', 'password': 'correctpassword'}
    response = client.post('/login', data=data)

    assert response.status_code == 200  # Expect a successful login
    assert b'Welcome, existinguser' in response.data  # Check if welcome message is present
# More tests for other routes, form submissions, database interactions, etc. can be added here


# Scenario 2: Data science project - Building trust in your models
import pytest
import pandas as pd
from your_data_science_project import clean_data, train_model, predict

# Sample test data
@pytest.fixture
def test_data():
    data = {'feature1': [1, 2, 3, None], 'feature2': ['A', 'B', 'C', 'D']}
    return pd.DataFrame(data)

def test_data_cleaning(test_data):
    """Verify if data cleaning handles missing values correctly."""
    cleaned_data = clean_data(test_data)
    assert cleaned_data['feature1'].isnull().sum() == 0  # Check if missing values are filled

def test_model_predictions():
    """Check if model predictions match expected outcomes."""
    X_test = ...  # Load your test data
    y_test = ...  # Load corresponding ground truth labels
    model = train_model(...) 
    predictions = predict(model, X_test)
    accuracy = (predictions == y_test).mean()
    assert accuracy > 0.8  # Set your desired accuracy threshold

def test_model_performance():
    """Evaluate model performance using relevant metrics."""
    # ... Load your evaluation data and calculate metrics (e.g., precision, recall, F1-score)
    # Assert that the metrics meet your expectations
    
  
import pytest

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Division by zero!")
        return x / y

class CalculatorTest:
    @pytest.fixture
    def calculator(self):
        from calculator import Calculator
        return Calculator()

    def test_add(self, calculator):
        result = calculator.add(2, 3)
        assert result == 5

    def test_subtract(self, calculator):
        result = calculator.subtract(5, 2)
        assert result == 3

    def test_multiply(self, calculator):
        result = calculator.multiply(4, 3)
        assert result == 12

    def test_divide(self, calculator):
        result = self.calculator.divide(10, 2)
        assert result == 5

    def test_divide_by_zero(self, calculator):
        with pytest.raises(ValueError):
            calculator.divide(5, 0)

import pytest

class Product:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity

class Cart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, product):
        self.items.append(product)

    def calculate_total_price(self, tax_rate=0.0, shipping_fee=0.0):
        subtotal = sum(item.price * item.quantity for item in self.items)
        tax = subtotal * tax_rate
        total = subtotal + tax + shipping_fee
        return total

    def apply_discount(self, discount_percentage):
        for item in self.items:
            item.price *= (1 - discount_percentage / 100)

    def checkout(self, payment_gateway):
        total_price = self.calculate_total_price()
        # In a real application, you'd interact with the payment_gateway here
        if payment_gateway.process_payment(total_price):
            # Place the order (logic not shown here)
            return True
        else:
            return False

class TestProductFunctions:
    def test_add_to_cart_successful(self):
        cart = Cart()
        product = Product("Widget", 10.0)
        cart.add_to_cart(product)
        assert len(cart.items) == 1
        assert cart.items[0] == product

    def test_calculate_total_price_accuracy(self):
        cart = Cart()
        cart.add_to_cart(Product("Widget A", 15.0))
        cart.add_to_cart(Product("Widget B", 20.0, 2))  # 2 of these
        total = cart.calculate_total_price(tax_rate=0.07, shipping_fee=5.0)
        expected_total = (15.0 + 20.0 * 2) * 1.07 + 5.0
        assert total == expected_total

    def test_apply_discount_correctly(self):
        cart = Cart()
        cart.add_to_cart(Product("Discounted Item", 50.0))
        cart.apply_discount(20)  # 20% discount
        assert cart.items[0].price == 40

    def test_checkout_successful_payment(self, mocker):
        # Mocking a payment gateway (would be a real integration in a production app)
        mock_payment_gateway = mocker.Mock()
        mock_payment_gateway.proces_payment.return_value = True

        cart = Cart()
        cart.add_to_cart(Product("Something", 100.0))
        result = cart.checkout(mock_payment_gateway)
        assert result is True # Checkout should be successful



'''
Parameterization lets you run the same test multiple times with different inputs.
This avoids writing duplicate test functions for each dataset.
Helps ensure your function works for many cases quickly.
'''
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (10, 5, 15),
    (-1, 1, 0),
])
def test_calculate_sum(a, b, expected):
    assert a + b == expected
