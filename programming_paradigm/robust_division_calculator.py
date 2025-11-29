def safe_divide(numerator, denominator):
    """
    Safely divide two numbers with error handling for:
    - Non-numeric input
    - Division by zero
    """

    # Try converting inputs to floats
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."
    # Try performing division
    try:
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
