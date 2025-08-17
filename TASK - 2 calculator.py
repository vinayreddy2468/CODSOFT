# function for addition
def add(a,b):
    return a + b

# function for subtraction
def subtract(a,b):
    return a - b

# function for multipication
def multiply(a,b):
    return a * b

# function for  division
def divide(a,b):
    if b==0 :
        return 'error:dividing by zero'
    return a / b

#Main calc function
def calculator():
    while True:
        print("\n   Simple Calculator ")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice(1-5): ")
        if choice == '5':
            print("Exiting")
            break

        try:
            num1=float(input("Enter the first number: "))
            num2=float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input Enter numbers only")
            continue
        
        if choice =='1':
            print(f"Result: {add(num1,num2)}")
        elif choice == '2':
            print(f"Result: {subtract(num1,num2)}")
        elif choice == '3':
            print(f"Result: {multiply(num1,num2)}")
        elif choice == '4':
            print(f"Result: {divide(num1,num2)}")
        else:
            print("Invalid choice. Please select from (1-5)")
calculator()
