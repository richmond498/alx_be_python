FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9      # multiply after subtracting 32
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5      # multiply then add 32


def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using global FAHRENHEIT_TO_CELSIUS_FACTOR.
    Formula: (F - 32) * (5/9)
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using global CELSIUS_TO_FAHRENHEIT_FACTOR.
    Formula: C * (9/5) + 32
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def _prompt_and_convert():
    """
    Prompt user for temperature and unit, perform conversion, and print result.
    Raises ValueError with exact message if temperature is not numeric.
    """
    temp_input = input("Enter the temperature to convert: ").strip()

    # Validate numeric temperature
    try:
        temperature = float(temp_input)
    except ValueError:
        # exact error message required by your spec
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "F":
        result = convert_to_celsius(temperature)
        print(f"{temperature}°F is {result}°C")
    elif unit == "C":
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {result}°F")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")


if __name__ == "__main__":
    # Run the interactive prompt once
    _prompt_and_convert()

    # --- quick demonstrations / smoke tests (not interactive) ---
    # These show the factors are working (prints are optional; remove if undesired)
    print("\n-- Demo conversions --")
    print("100°F ->", convert_to_celsius(100), "°C")   # expected ~37.77777777777778
    print("32°F ->", convert_to_celsius(32), "°C")     # expected 0.0
    print("0°C ->", convert_to_fahrenheit(0), "°F")    # expected 32.0
    print("100°C ->", convert_to_fahrenheit(100), "°F")# expected 212.0
