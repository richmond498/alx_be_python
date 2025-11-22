from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()

    # Format the date and time as YYYY-MM-DD HH:MM:SS
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

    print(f"Current date and time: {formatted_date}")


def calculate_future_date():
    # Prompt user for number of days
    days_to_add = int(input("Enter the number of days to add to the current date: "))

    # Get today's date
    today = datetime.now()

    # Add the number of days using timedelta
    future_date = today + timedelta(days=days_to_add)

    # Print in YYYY-MM-DD format
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")


# ---- Main Program ----
if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
