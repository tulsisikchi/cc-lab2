def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def calculator():
    print("Simple Calculator")
    print("Operations: +  -  *  /")

    while True:
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operation (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if op == '+':
                print("Result:", add(num1, num2))
            elif op == '-':
                print("Result:", subtract(num1, num2))
            elif op == '*':
                print("Result:", multiply(num1, num2))
            elif op == '/':
                print("Result:", divide(num1, num2))
            else:
                print("Invalid operation")

        except ValueError:
            print("Invalid input. Please enter numbers.")

        again = input("Do you want to calculate again? (y/n): ")
        if again.lower() != 'y':
            break

if __name__ == "__main__":
    calculator()
