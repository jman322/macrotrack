import csv
import os
from colored import Fore, Back, Style
from datetime import datetime
from time import sleep
import pandas as pd
import numpy as np



def create_menu():
    os.system('cls||clear')
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

def filecheck():
    fieldnames = ['Date', 'Breakfast Calories','Breakfast Protein','Lunch Calories','Lunch Protein','Dinner Calories','Dinner Protein','Snack Calories','Snack Protein','Total Calories', 'Total Protein']
    file_path = 'data/meals.csv'

    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        # If the file doesn't exist or is empty, write the header
        with open(file_path, mode='w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
    else:
        # File exists, let's check the existing fieldnames
        with open(file_path, mode='r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            existing_fieldnames = next(reader, None)  # Read the first line (header)

        # Only write the header if it doesn't match the current fieldnames
        if existing_fieldnames != fieldnames:
            with open(file_path, mode='w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()



def addmacro(mealcalories, mealprotein):


    filecheck()



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

        if pd.notna(df.at[row_index, mealcalories]):
            os.system('cls||clear')
            print(f'{mealcalories} is already input. Would you like to update?')
            print('Enter 1 for Yes')
            print('Enter 2 for No')

            userinput = input("Enter your choice: ")

            if userinput == '1':
                df.at[row_index, mealcalories] = int(Calories)
            elif userinput == '2':
                df.at[row_index, mealcalories] = int(df.at[row_index, mealcalories])
            else:
                print('Invalid Input')
        else:
            df[mealcalories] = df[mealcalories].fillna(0).astype(int)
            df.at[row_index, mealcalories] = int(Calories)

        if pd.notna(df.at[row_index, mealprotein]):
            os.system('cls||clear')
            print(f'{mealprotein} is already input. Would you like to update?')
            print('Enter 1 for Yes')
            print('Enter 2 for No')

            userinput = input("Enter your choice: ")

            if userinput == '1':
                df.at[row_index, mealprotein] = int(Protein)
            elif userinput == '2':
                df.at[row_index, mealprotein] = int(df.at[row_index, mealprotein])
            else:
              print('Invalid Input')
        else:
            df[mealprotein] = df[mealprotein].fillna(0).astype(int)
            df.at[row_index, mealprotein] = int(Protein)
    else:
        #if the date is not already present in csv create a new row for it
        new_row = {
            'Date': todays_date,
            mealcalories: int(Calories),
            mealprotein: int(Protein)
        }
        df = df._append(new_row, ignore_index=True)


    df['Total Calories'] = (df['Breakfast Calories'].fillna(0) + df['Lunch Calories'].fillna(0) + df['Dinner Calories'].fillna(0) + df['Snack Calories'].fillna(0))
    df['Total Calories'] = df['Total Calories'].fillna(0).astype(int)

    df['Total Protein'] = (df['Breakfast Protein'].fillna(0) + df['Lunch Protein'].fillna(0) + df['Dinner Protein'].fillna(0) + df['Snack Protein'].fillna(0))
    df['Total Protein']  = df['Total Protein'].fillna(0).astype(int)

    #Ensure all edited fields are int and not float
    df[mealcalories] = df[mealcalories].fillna(0).astype(int)
    df[mealprotein] = df[mealprotein].fillna(0).astype(int)

    df.to_csv('data/meals.csv', index=False)
    return

def addsnack(mealcalories, mealprotein):

    
    filecheck()



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

        if pd.notna(df.at[row_index, mealcalories]):
            os.system('cls||clear')
            print(f'{mealcalories} is already input. Would you like to update, add a snack or go back?')
            print('Enter 1 for Update')
            print('Enter 2 for Add')
            print('Enter 3 to go Back')

            userinput = input("Enter your choice: ")

            if userinput == '1':
                df.at[row_index, mealcalories] = int(Calories)
            elif userinput == '2':
                df.at[row_index, mealcalories] =+ int(Calories)
            elif userinput == '3':
                pass              
            else:
                print('Invalid Input')
        else:
            df[mealcalories] = df[mealcalories].fillna(0).astype(int)
            df.at[row_index, mealcalories] = int(Calories)

        if pd.notna(df.at[row_index, mealprotein]):
            os.system('cls||clear')
            print(f'{mealcalories} is already input. Would you like to update, add a snack or go back?')
            print('Enter 1 for Update')
            print('Enter 2 for Add')
            print('Enter 3 to go Back')

            userinput = input("Enter your choice: ")

            if userinput == '1':
                df.at[row_index, mealprotein] = int(Protein)
            elif userinput == '2':
                df.at[row_index, mealprotein] =+ int(Protein)
            elif userinput == '3':
                pass
            else:
              print('Invalid Input')
        else:
            df[mealprotein] = df[mealprotein].fillna(0).astype(int)
            df.at[row_index, mealprotein] = int(Protein)
    else:
        #if the date is not already present in csv create a new row for it
        new_row = {
            'Date': todays_date,
            mealcalories: int(Calories),
            mealprotein: int(Protein)
        }
        df = df._append(new_row, ignore_index=True)

    df['Total Calories'] = (df['Breakfast Calories'].fillna(0) + df['Lunch Calories'].fillna(0) + df['Dinner Calories'].fillna(0) + df['Snack Calories'].fillna(0))
    df['Total Calories'] = df['Total Calories'].fillna(0).astype(int)
    
    df['Total Protein'] = (df['Breakfast Protein'].fillna(0) + df['Lunch Protein'].fillna(0) + df['Dinner Protein'].fillna(0) + df['Snack Protein'].fillna(0))
    df['Total Protein']  = df['Total Protein'].fillna(0).astype(int)

    #Ensure all edited fields are int and not float
    df[mealcalories] = df[mealcalories].fillna(0).astype(int)
    df[mealprotein] = df[mealprotein].fillna(0).astype(int)

    df.to_csv('data/meals.csv', index=False)
    return

def addmeal():
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
                addsnack('Snack Calories', 'Snack Protein')
                os.system('cls||clear')
                addmeal()
            if choice == "5":
                create_menu()
            else:
                print('Invalid Choice')
                addmeal()


def delmeal():
    count = 1
    df = pd.read_csv('data/meals.csv')

    print('\nWhich Day would you like to select?\n')

    for date in df['Date'].values:
        print(f'Enter {count} for {date}')
        count += 1

    userinput = int(input("Enter your choice: "))
    

    if not userinput > count-1 and userinput > 0:
        os.system('cls||clear')
        date_chosen = df['Date'].iloc[int(userinput) - 1]

        print('\nWhich Field Would you like to delete?\n')

        
        print('Enter 1 for Breakfast Calories')
        print('Enter 2 for Breakfast Protein')
        print('Enter 3 for Lunch Calories')
        print('Enter 4 for Lunch Protein')
        print('Enter 5 for Dinner Calories')
        print('Enter 6 for Dinner Protein')
        print('Enter 7 for Snack Calories')
        print('Enter 8 for Snack Protein')
        print('Enter 9 for Total Calories')
        print('Enter 10 for Total Protein')

        choice = input('Enter Choice: ')
        row_index = df.index[df['Date'] == date_chosen].tolist()[0]
        if choice == '1':
            df.at[row_index, 'Breakfast Calories'] = np.nan
            df.to_csv('data/meals.csv', index=False)
            print("\n'Breakfast Calories set to NaN")
            delmeal()
        elif choice == '2':
            df.at[row_index, 'Breakfast Protein'] = np.nan
            df.to_csv('data/meals.csv', index=False)
            print("\n'Breakfast Protein set to NaN")
            delmeal()
        elif choice == '3':
            df.at[row_index, 'Lunch Calories'] = np.nan
            df.to_csv('data/meals.csv', index=False)
            print("\n'Lunch Calories set to NaN")
            delmeal()
        elif choice == '4':
            df.at[row_index, 'Lunch Protein'] = np.nan
            df.to_csv('data/meals.csv', index=False)
            print("\n'Lunch Protein set to NaN")
            delmeal()
        elif choice == '5':
            df.at[row_index, 'Dinner Calories'] = np.nan
            df.to_csv('data/meals.csv', index=False)
            print("\n'Dinner Calories set to NaN")
            delmeal()
        elif choice == '6':
            df.at[row_index, 'Dinner Protein'] = np.nan
            df.to_csv('data/meals.csv', index=False)
            print("\n'Dinner Protein set to NaN")
            delmeal()
        elif choice == '7':
            df.at[row_index, 'Snack Calories'] = np.nan
            df.to_csv('data/meals.csv', index=False)
            print("\n'Snack Calories set to NaN")
            delmeal()
        elif choice == '8':
            df.at[row_index, 'Snack Protein'] = np.nan
            df.to_csv('data/meals.csv', index=False)
            print("\n'Snack Protein set to NaN")
            delmeal()
        elif choice == '9':
            df.at[row_index, 'Total Calories'] = np.nan
            df.to_csv('data/meals.csv', index=False)
            print("\n'Total Calories set to NaN")
            delmeal()
        elif choice == '10':
            df.at[row_index, 'Total Protein'] = np.nan
            df.to_csv('data/meals.csv', index=False)
            print("\n'Total Protein set to NaN")
            delmeal()
        else:
            print("Invalid choice")
    else:
        print('\nInvalid Input')
        delmeal()

def printdf():
    df = pd.read_csv('data/meals.csv')
    print(df)
    userinput = input('Enter 0 to go back: ')
    if userinput == '0':
        create_menu()
    else:
        print('\nInvalid Input\n')
        printdf()


def calcalc():

    weight = int(input('Enter Weight(kg):'))

    height = int(input('Enter Height(cm): '))

    age = int(input('Enter Age: '))

    print('Enter 1 For Male')
    print('Enter 2 For Female')
    gender = int(input('Enter Choice: '))

    if gender == 1:
        BMR = 10 * weight + 6.25 * height - 5 * age + 5
    elif gender == 2:
        BMR = 10 * weight + 6.25 * height - 5 * age - 161
    else:
        print('Invalid Choice')
        calcalc
   
    print('\nEnter Activity Level\n')
    print('Enter 1 for Sedentary: Little to no exercise')
    print('Enter 2 for Light: Light exercise 1-3 times a week')
    print('Enter 3 for Moderate: Moderate exercise 4-5 times a week')
    print('Enter 4 for Active: Daily exercise or intense workouts 3+')
    print('Enter 5 for Very Active: Intense exercise 6-7 times a week or very physically demanding job')
    choice = input('Enter Choice: ')

    if choice == '1':
        TDEE = BMR * 1.2
    elif choice == '2':
        TDEE = BMR * 1.375
    elif choice == '3':
        TDEE = BMR * 1.55
    elif choice == '4':
        TDEE = BMR * 1.725
    elif choice == '5':
        TDEE = BMR * 1.9
    else:
        print('Invalid choice, using Sedentary as default.')
        TDEE = BMR * 1.2


    print(f"Your Total Daily Energy Expenditure (TDEE) is: {TDEE} calories/day")
    print(f"For mild weight loss (0.25kg/week) consume {0.9* TDEE}")
    print(f"For weight loss (0.5kg/week) consume {0.79 * TDEE}")
    print(f"For mild weight gain (0.25kg/week) consume {1.1 * TDEE}")

calcalc()