number = int(input("Enter a number to see its multiplication table:"))


for X in range(1, 11):
    Z = X * number
    print(f"{number} * {X}= {Z}")
