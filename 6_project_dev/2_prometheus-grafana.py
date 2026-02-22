"""
prometheus --config.file=prometheus.yml

brew services start/stop grafana
"""

from prometheus_client import Counter, start_http_server

# Create a metric to track the number of calculations performed.
calculations = Counter("calculations_total", "Total number of calculations performed")


def add(x, y):
    """Adds two numbers and increments the calculations counter."""
    calculations.inc()
    return x + y


def subtract(x, y):
    """Subtracts two numbers and increments the calculations counter."""
    calculations.inc()
    return x - y


def multiply(x, y):
    """Multiplies two numbers and increments the calculations counter."""
    calculations.inc()
    return x * y


def divide(x, y):
    """Divides two numbers and increments the calculations counter."""
    if y == 0:
        return "Division by zero!"
    calculations.inc()
    return x / y


if __name__ == "__main__":
    # Start the Prometheus metrics server on port 8000.
    start_http_server(8000)

    # Keep the application running indefinitely.
    while True:
        pass
