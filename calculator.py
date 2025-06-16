def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Cannot divide by zero."
    return x / y

def exponent(x, y):
    return x ** y

def modulus(x, y):
    if y == 0:
        return "Error! Cannot mod by zero."
    return x % y

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")

def calculator():
    print("🔢 Welcome to the Python CLI Calculator!")

    result = None  # This will hold the previous result

    while True:
        print("\nChoose operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exponent (^)")
        print("6. Modulus (%)")
        print("7. Exit")

        choice = input("Enter choice (1–7): ").strip()

        if choice == '7':
            print("👋 Exiting calculator. Goodbye!")
            break

        # Check for valid choice
        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("❌ Invalid choice. Please choose from 1 to 7.")
            continue

        # Use previous result or new number
        if result is not None:
            use_previous = input(f"\nUse previous result ({result}) as first number? (y/n): ").lower()
            if use_previous == 'y':
                num1 = result
            else:
                num1 = get_number("Enter first number: ")
        else:
            num1 = get_number("Enter first number: ")

        num2 = get_number("Enter second number: ")

        # Perform calculation
        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)
        elif choice == '5':
            result = exponent(num1, num2)
        elif choice == '6':
            result = modulus(num1, num2)

        print(f"\n✅ Result: {result}")

# Run the calculator
calculator()
