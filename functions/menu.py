import os
from functions import meal_manager

class Menu:
    def __init__(self, options):
        self.options = options
        
    
    def display(self):
        os.system('cls||clear')
        for key, option in self.options.items():
            print(f"{key}. {option[0]}")
            
    def get_user_choice(self, meal_manager):
        choice = int(input("Enter your choice: "))
        if choice in self.options:
            self.options[choice][1](meal_manager)
        else:
            print("Invalid choice.")
            

