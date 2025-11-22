def perform_operation(num1, num2, operation):
    if operation == "add":
        num1 + num2
    elif operation == "subtract":
        num1 - num2
    elif operation == "multiply":
        num1 * num2 
    elif operation == "divide" and num2 == 0:
        print(f"num2 can not be zero")
    elif operation == "divide":
        num1/num2

    