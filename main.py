import os
from colored import Fore, Back, Style
from functions.funcs import addmeal, addmacro, addsnack, create_menu, delmeal, printdf, calcalc, procalc, comparegoals


print(f"{Fore.green}Welcome to the Macrotrack!{Style.reset}\n")

choice = ""

while choice != "7":
    choice = create_menu()

    if choice == "1":
        os.system('cls||clear')
        addmeal()
    elif choice == "2":
        os.system('cls||clear')
        delmeal()
    elif choice == "3":
        os.system('cls||clear')
        printdf()
    elif choice == "4":
        os.system('cls||clear')
        calcalc
    elif choice == "5":
        os.system('cls||clear')
        procalc()
    elif choice == "6":
        os.system('cls||clear')
        comparegoals()
    elif choice == "7":
        print('Save and Exit')
    else:
        print("invalid choice")

print("Thankyou for using Macrotrack")
