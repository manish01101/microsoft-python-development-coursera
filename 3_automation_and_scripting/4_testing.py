"""
Docstring for 3_automation_and_scripting.4_testing

types:
unit: individual units
integration: examines the connections and communication pathways between different modules or components
e2e

regression
usability testing

unit testing libraries:
1. pytest (third party): gained popularity due to its simplicity, flexibility, and powerful features like fixtures and parametrization.
2. unittest (Python standard library):
"""

import unittest


def calculate_total(price, tax_rate):
    return price + (price * tax_rate)


class TestCalculateTotal(unittest.TestCase):
    def test_calculate_total(self):
        # Example unit test
        self.assertEqual(calculate_total(100, 0.05), 105)

    def test_calculate_total_no_tax(self):
        # Example unit test
        self.assertEqual(calculate_total(200, 0), 200)


unittest.main()


import pytest
import requests


def test_integration_api():
    response = requests.get("https://api.example.com/customers")
    assert response.status_code == 200
    assert "customers" in response.json()


if __name__ == "__main__":
    pytest.main()
