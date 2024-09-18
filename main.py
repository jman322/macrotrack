import os
from colored import Fore, Back, Style

print(f"{Fore.green}Welcome to the Macrotrack!{Style.reset}\n")

def create_menu():
    print("Enter 1 to Add Meal")
    print("Enter 2 to Delete Meal")
    print("Enter 3 to List Meal History")
    print("Enter 4 to Calculate Target Calories")
    print("Enter 5 to Calculate Target Protien")
    print("Enter 6 to View Progress")
    print('Enter 7 to Save and Exit\n')


    choice = input("Enter your choice: ")

    print(choice)

    return choice

choice = ""

while choice !=  "7":
    choice = create_menu()

    if choice == "1":
        print('Add Meal')
    elif choice == "2":
        print('Delete Meal')
    elif choice == "3":
        print('List Meal History')
    elif choice == "4":
        print('Calc Target Cals')
    elif choice == "5":
        print('Calc Target Pro')
    elif choice == "6":
        print('View Progress')
    elif choice == "7":
       print('Save and Exit')
    else:
        print("invalid choice")

print("Thankyou for using Macrotrack")