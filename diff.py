import math

print("Choose function:")
print("1. x^2")
print("2. x^3")
print("3. sin(x)")

choice = int(input("Enter choice: "))

def f(x):
    if choice == 1:
        return x**2
    elif choice == 2:
        return x**3
    elif choice == 3:
        return math.sin(x)

def derivative(x, h=0.0001):
    return (f(x + h) - f(x - h)) / (2 * h)

x = float(input("Enter value of x: "))
print("Derivative =", derivative(x))
