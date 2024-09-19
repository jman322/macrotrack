import csv
import os
from colored import Fore, Back, Style
from datetime import datetime
from time import sleep
import pandas as pd

def addmacro(mealcalories, mealprotein):
    with open('data/meals.csv', mode='a', newline='') as csvfile:
        fieldnames = ['Date', 'Breakfast Calories','Breakfast Protein','Lunch Calories','Lunch Protein','Dinner Calories','Dinner Protein','Snack Calories','Snack Protein','Total Caloriees', 'Total Protein']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
              
        while True:
            Calories = input('Enter Calories: ')
            try:
                int_value = int(Calories)
                break
            except ValueError:
                print("Please input a valid number for Calories.")
        while True:
            Protein = input('Enter Protein: ')
            try:
                int_value = int(Protein)
                break
            except ValueError:
                print("Please input a valid number for Protein.")




    df = pd.read_csv('data/meals.csv')

    todays_date = datetime.now().strftime('%Y-%m-%d')
    if todays_date in df['Date'].values:
        row_index = df.index[df['Date'] == todays_date].tolist()[0]
        df.at[row_index, mealcalories] = Calories
        df.at[row_index, mealprotein] = Protein

        df.to_csv('data/meals.csv', index=False)

            


        

    return



def addmeal():



        formatted_date = datetime.now().strftime('%Y-%m-%d')

        print(formatted_date)




        print('\nWhich meal Would You like to add?\n')
        print('Enter 1 for Breakfast')
        print('Enter 2 for Lunch')
        print('Enter 3 for Dinner')
        print('Enter 4 for Snack')
        print('Enter 5 to go Back to Main Menu\n')
        
        choice = input("Enter your choice: ")

        while choice != "5":
            if choice == "1":
                addmacro('Breakfast Calories', 'Breakfast Protein')
                os.system('cls||clear')
                addmeal()
            if choice == "2":
                addmacro('Lunch Calories', 'Lunch Protein')
                os.system('cls||clear')
                addmeal()
            if choice == "3":
                addmacro('Dinner Calories', 'Dinner Protein')
                os.system('cls||clear')
                addmeal()           
            if choice == "4":
                pass
            if choice == "5":
                pass

addmeal()
