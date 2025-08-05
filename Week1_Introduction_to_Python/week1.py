# Week 1: Introduction to Python Programming

def temperature_converter():
    print("\n--- Temperature Converter ---")
    choice = input("Convert to (C/F)? ").strip().upper()
    temp = float(input("Enter temperature: "))

    if choice == 'C':
        print(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
    elif choice == 'F':
        print(f"{temp}°C = {(temp * 9/5) + 32:.2f}°F")
    else:
        print("Invalid choice!")

def calculator():
    print("\n--- Calculator ---")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")

    if op == '+':
        print(a + b)
    elif op == '-':
        print(a - b)
    elif op == '*':
        print(a * b)
    elif op == '/':
        print("Error: Division by zero!" if b == 0 else a / b)
    else:
        print("Invalid operation!")

def average_temperature():
    print("\n--- Average Temperature ---")
    temps = [float(t) for t in input("Enter temperatures: ").split()]
    print(f"Average Temperature: {sum(temps) / len(temps):.2f}")

if __name__ == "__main__":
    temperature_converter()
    calculator()
    average_temperature()
