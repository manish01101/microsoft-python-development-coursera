'''
Naming considerations : use snake_case
If a function is intended for internal use within a module and shouldn't be accessed directly from outside, prefix its name with an underscore (_). For instance, _calculate_internal_metrics. For functions that return a boolean value (True/False), strongly consider using prefixes like is_, has_, or can_ to instantly signal their nature. 
'''

'''
The Anatomy of an Exemplary Docstring
Purpose
Arguments: A detailed list of all input parameters
Return value
Exception handling
Examples (Optional)
'''
def calculate_monthly_payment(principal: float, interest_rate: float, loan_term_years: int) -> float:
    """
    Calculates the monthly payment for a fixed-rate loan.

    Args:
        principal: The total amount borrowed (float).
        interest_rate: The annual interest rate (as a decimal, float).
        loan_term_years: The loan term in years (int).

    Returns:
        The monthly payment amount (float).

    Raises:
        ValueError: If any of the inputs are negative or zero.

    Example:
        >>> calculate_monthly_payment(100000, 0.05, 30)
        530.33 
    """
    if principal <= 0 or interest_rate <= 0 or loan_term_years <= 0:
        raise ValueError("All input values must be positive.")

    monthly_interest_rate = interest_rate / 12
    number_of_payments = loan_term_years * 12
    
    # Calculation logic for monthly payment (omitted for brevity)

    return monthly_payment

'''
Why pure functions with argument passing matter
they only use the information you give them directly (their inputs), and they don't change anything outside of themselves
perfect for running tasks at the same time (parallel processing), as they won't accidentally step on each other's toes by changing shared data.
'''

'''
Variable Number of Arguments (*args and **kwargs) 
Python allows you to define functions that accept a variable number of arguments. You can use *args to collect positional arguments into a tuple and **kwargs to collect keyword arguments into a dictionary.
'''
def flexible_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

flexible_function(1, 2, 3, name="Alice", age=30)