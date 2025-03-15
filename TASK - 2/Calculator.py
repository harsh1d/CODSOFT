"""
Design a simple calculator with basic arithmetic operations.
Prompt the user to input two numbers and an operation choice.
Perform the calculation and display the result
"""
import datetime
import os

def display_menu():
    print("Calculator Menu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("Enter your choice (1-5):")
    
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero"
    return num1 / num2

def main():
    timestamp = datetime.datetime.now().strftime("%d-%m-%Y_%H%M%S")
    folder_path = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(folder_path, f"calculation_results_{timestamp}.txt")
    with open(filename, "a") as file:
        while True:
            display_menu()
            choice = int(input())
            
            if choice == 5:
                break
            
            if choice < 1 or choice > 5:
                print("Invalid choice. Please try again.")
                continue
            
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            if choice == 1:
                result = add(num1, num2)
                operation = "Addition"
            elif choice == 2:
                result = subtract(num1, num2)
                operation = "Subtraction"
            elif choice == 3:
                result = multiply(num1, num2)
                operation = "Multiplication"
            elif choice == 4:
                result = divide(num1, num2)
                operation = "Division"
            else:
                print("Invalid choice. Please try again.")
                continue
            
            print(f"Result: {result}")
            file.write(f"{operation} of {num1} and {num2} = {result}\n")
            
if __name__ == "__main__":
    main()