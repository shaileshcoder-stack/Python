
# 1) Take 2 inputs from the user as a integers, check whether both are equal or not (if-else)
number1 =int(input("number one :"))
number2 =int(input("number two :"))

if number1==number2 :
    print("value is same")

else:
     print("value is diffrent")

# 2) Print 1 to 100 number with help of range() and for loop, in that(1-100) print only odd numbers?(if)
numbers =(range(1,100,1))
for i in numbers:
    if i%2 !=0:
        print("values",i)



# 3) write a program check that given string is in lowercase or not ? (if)

textvalue = str(input("Enter the text :"))

if (textvalue.islower()):
    print("value of :is lower case"),
else:
    print("value of :is Upper case")



# 4) write a program print Menu card lik
def print_menu():
    print("step:-1")
    print("-------")
    print("1. add")
    print("2. sub")
    print("3. multiplication")
    print("4. division")

def get_user_choice():
    return int(input("Enter your choice (1-4): "))

def perform_operation(choice):
    if choice in [1, 2, 3, 4]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print(f"Result: {num1 + num2}")
        elif choice == 2:
            print(f"Result: {num1 - num2}")
        elif choice == 3:
            print(f"Result: {num1 * num2}")
        elif choice == 4:
            if num2 != 0:
                print(f"Result: {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed.")
    else:
        print("Invalid input")

if __name__ == "__main__":
    print_menu()
    user_choice = get_user_choice()
    perform_operation(user_choice)
