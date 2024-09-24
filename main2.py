from functions.menu import Menu
from functions.file_manager import FileManager
from functions.meal_manager import MealManager
import os


import os
from datetime import datetime

fieldnames = [
    'Date',
    'Breakfast Calories',
    'Breakfast Protein',
    'Lunch Calories',
    'Lunch Protein',
    'Dinner Calories',
    'Dinner Protein',
    'Snack Calories',
    'Snack Protein',
    'Total Calories',
    'Total Protein'
]
file_path = 'data/meals.csv'
file_manager = FileManager('data/meals.csv', fieldnames)
file_manager.check_file() 
file_manager.validate_file()

meal_manager = MealManager(file_manager)

def addmeal(meal_manager):
    os.system('cls')
    meal_options = {
        "1": {"type": "breakfast", "calories": "Breakfast Calories", "protein": "Breakfast Protein"},
        "2": {"type": "lunch", "calories": "Lunch Calories", "protein": "Lunch Protein"},
        "3": {"type": "dinner", "calories": "Dinner Calories", "protein": "Dinner Protein"},
        "4": {"type": "snack", "calories": "Snack Calories", "protein": "Snack Protein"}
    }

    print('\nWhich meal would you like to add?\n')
    for key, meal in meal_options.items():
        print(f"Enter {key} for {meal['type'].capitalize()}")
    print('Enter 5 to go Back to Main Menu\n')

    choice = input("Enter your choice: ")

    if choice in meal_options:
        meal_manager.add_meal(meal_options[choice]['type'], meal_options[choice]['calories'], meal_options[choice]['protein'])
        return
    elif choice == "5":
        return
    else:
        print('Invalid Choice')
        addmeal(meal_manager)


menu_options = {
    1: ("Add Meal", addmeal),
    2: ("Delete Meal", addmeal),
    3: ("List Meal History", addmeal),
    4: ("Calculate Target Calories", addmeal),
    5: ("Calculate Target Protein", addmeal),
    6: ("View Progress", addmeal),
    7: ("Save and Exit", addmeal)
}
menu = Menu(menu_options)
while True:
    menu.display()
    user_choice = menu.get_user_choice(meal_manager)

    # You may want to break the loop if user_choice is "Exit"
    if user_choice == 7:
        print("Exiting the program...")
        break

