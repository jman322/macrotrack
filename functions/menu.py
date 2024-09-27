import os
from functions import meal_manager


class Menu:
    def __init__(self, options):
        self.options = options

    def display(self):
        os.system('cls||clear')
        print("""
███╗░░░███╗░█████╗░░█████╗░██████╗░░█████╗░████████╗██████╗░░█████╗░░█████╗░██╗░░██╗
████╗░████║██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
██╔████╔██║███████║██║░░╚═╝██████╔╝██║░░██║░░░██║░░░██████╔╝███████║██║░░╚═╝█████═╝░
██║╚██╔╝██║██╔══██║██║░░██╗██╔══██╗██║░░██║░░░██║░░░██╔══██╗██╔══██║██║░░██╗██╔═██╗░
██║░╚═╝░██║██║░░██║╚█████╔╝██║░░██║╚█████╔╝░░░██║░░░██║░░██║██║░░██║╚█████╔╝██║░╚██╗
╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝\n"""
        )
        for key, option in self.options.items():
            print(f"{key}. {option[0]}")

    def get_user_choice(self, meal_manager=None):

        while True:
            try:
                choice = int(input("Enter your choice: "))
                break
            except ValueError:
                os.system('cls||clear')
                print('Invalid input. Please input a number.')
                return
        if choice in self.options:
            # Check if the function requires 'meal_manager'
            func = self.options[choice][1]
            if meal_manager and func.__code__.co_argcount > 0:  # If the function expects arguments
                os.system('cls||clear')
                func(meal_manager)  # Pass meal_manager
            else:
                os.system('cls||clear')
                func()  # No arguments needed
        else:
            os.system('cls||clear')
            print("Invalid choice.")
