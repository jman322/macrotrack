from functions.menu import Menu
from functions.file_manager import FileManager
from functions.meal_manager import MealManager
from functions.calculator import Calculator
import os
from colorama import Fore, Style
from datetime import datetime

os.system('cls||clear')
print(Fore.CYAN)

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

def calculate_tdee():
    while True:
        try:
            print('Enter 0 to return')
            weight = int(input('Enter Weight(kg): '))
            if weight == 0:
                return  # Exits the function if user inputs 0
            height = int(input('Enter Height(cm): '))
            age = int(input('Enter Age: '))
            break
        except ValueError:
            print('Invalid Input. Please input a number')

    while True:
        try:
            print('Enter 1 for Male')
            print('Enter 2 for Female')
            gender = int(input('Enter Choice: '))
            if gender not in [1, 2]:
                raise ValueError  # Forces user to input a valid gender
            break
        except ValueError:
            print('Invalid Input. Please input a number')

    # Calculator instance handles the TDEE calculation and display
    calculator = Calculator(weight, height, age, gender)
    tdee = calculator.calculate_tdee()
    calculator.display_tdee_results(tdee)
    input('Enter anything to return to main menu: ')

def compare_goals(meal_manager):
    meal_manager.compare_goals()

def calculate_protein():
    while True:
        try:
            print('Enter 0 to return')
            bodyweight = int(input('Enter body weight (kg): '))
            if bodyweight == 0:
                return  # Exits the function if user inputs 0
            break
        except ValueError:
            print('Invalid Input. Please input a number')

    Calculator.calculate_protein(bodyweight)
    input('Enter anything to return to main menu: ')

def addmeal(meal_manager):
    os.system('cls||clear')

    meal_options = {
        "1": {
            "type": "breakfast",
            "calories": "Breakfast Calories",
            "protein": "Breakfast Protein"},
        "2": {
            "type": "lunch",
            "calories": "Lunch Calories",
            "protein": "Lunch Protein"},
        "3": {
            "type": "dinner",
            "calories": "Dinner Calories",
            "protein": "Dinner Protein"},
        "4": {
            "type": "snack",
            "calories": "Snack Calories",
            "protein": "Snack Protein"}}

    print('\nWhich meal would you like to add?\n')
    for key, meal in meal_options.items():
        print(f"Enter {key} for {meal['type'].capitalize()}")
    print('Enter 5 to go Back to Main Menu\n')

    choice = input("Enter your choice: ")

    if choice in meal_options:
        meal_manager.add_meal(
            meal_options[choice]['type'],
            meal_options[choice]['calories'],
            meal_options[choice]['protein'])
        return
    elif choice == "5":  # Go back to the main menu
        return
    else:
        print('Invalid Choice')
        addmeal(meal_manager)  # keep asking again if the choice is invalid

def print_meal_history(meal_manager):
    meal_manager.print_meal_history()

s
def deletemeal(mealmanager):
    meal_manager.delete_meal()

menu_options = {
    1: ("Add Meal", addmeal),
    2: ("Delete Meal", deletemeal),
    3: ("List Meal History", print_meal_history),
    4: ("Calculate Target Calories", lambda: calculate_tdee()),
    5: ("Calculate Target Protein", lambda: calculate_protein()),
    6: ("View Progress", compare_goals),
    7: ("Exit", lambda: exit())
}

menu = Menu(menu_options)
while True:
    menu.display()
    user_choice = menu.get_user_choice(meal_manager)

    if user_choice == 7:
        print("Exiting the program...")
        break
