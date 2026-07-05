def calculator():
    try:
        # Take two numbers as input
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        op = input("Enter operator (+, -, *, /): ")

        # Perform calculation using if-elif-else
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            # Handle division by zero
            if num2 == 0:
                print("Error: Division by zero is not allowed!")
                return
            else:
                result = num1 / num2
        else:
            print("Invalid operator! Please use +, -, *, /")
            return

        print("Result:", result)

    except ValueError:
        print("Invalid input! Please enter numbers only.")

# Run calculator
calculator()
