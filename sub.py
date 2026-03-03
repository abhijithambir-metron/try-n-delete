def subtract_numbers(a, b):
    """Subtract the second number from the first and return the result."""
    return a - b

if __name__ == "__main__":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = subtract_numbers(num1, num2)
    print(f"The difference between {num1} and {num2} is: {result}")