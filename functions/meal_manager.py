from functions import file_manager
from datetime import datetime
import pandas as pd
import os

class MealManager:
    def __init__(self, file_manager):
        self.file_manager = file_manager  # Handles file operations (reading/writing meals data)

    def add_meal(self, meal_type, mealcalories, mealprotein):
        os.system('cls||clear')
        self.file_manager.check_file()  # Ensure the CSV file exists

        calories = self.get_user_input("Calories")  # Get calories input from the user
        protein = self.get_user_input("Protein")  # Get protein input from the user

        df = self.file_manager.read_file()  # Read the current CSV data

        todays_date = datetime.now().strftime('%Y-%m-%d')  # Get todays date

        # If the 'Date' column is missing create it
        if 'Date' not in df.columns:
            df['Date'] = ""

        # If todays date exists in the CSV update the meal
        if todays_date in df['Date'].values:
            row_index = df.index[df['Date'] == todays_date].tolist()[0]

            self.update_meal(
                df,
                row_index,
                mealcalories,
                mealprotein,
                calories,
                protein)
        else:
            # Add a new row for today's meal if the date doesn't exist in the CSV
            df = self.add_new_meal(
                df,
                todays_date,
                mealcalories,
                mealprotein,
                calories,
                protein)

        os.system('cls||clear')
        df = self.recalculate_totals(df)  # Recalculate totals for the day
        self.file_manager.write_file(df)  # Write the updated data back to the CSV

    def get_user_input(self, field_name):
        while True:
            value = input(f'Enter {field_name}: ')
            try:
                return int(value)  # ensure input integer
            except ValueError:
                print(f"Please input a valid number for {field_name}")

    def update_meal(self, df, row_index, mealcalories, mealprotein, calories, protein):
        # Handle snack calories specifically (allows user to replace or add to existing values)
        if mealcalories == "Snack Calories":
            if pd.isna(df.at[row_index, mealcalories]):  # If NaN, set to 0
                df.at[row_index, mealcalories] = 0
            if df.at[row_index, mealcalories] == 0:
                df.at[row_index, mealcalories] = calories
            else:
                print(f"The current value for {mealcalories} is {df.at[row_index, mealcalories]}")
                snack_option = input(f"Do you want to replace this value or add to it? (r = replace / a = add): ").lower()
                if snack_option == 'r':
                    df.at[row_index, mealcalories] = calories
                elif snack_option == 'a':
                    df.at[row_index, mealcalories] += calories

        # Handle snack protein specifically
        if mealprotein == "Snack Protein":
            if pd.isna(df.at[row_index, mealprotein]):  # If NaN set to 0
                df.at[row_index, mealprotein] = 0
            if df.at[row_index, mealprotein] == 0:
                df.at[row_index, mealprotein] = protein
            else:
                print(f"The current value for {mealprotein} is {df.at[row_index, mealprotein]}")
                snack_option = input(f"Do you want to replace this value or add to it? (r = replace / a = add): ").lower()
                if snack_option == 'r':
                    df.at[row_index, mealprotein] = protein
                elif snack_option == 'a':
                    df.at[row_index, mealprotein] += protein

        # Handle non-snack calories
        if mealcalories != "Snack Calories":
            if pd.isna(df.at[row_index, mealcalories]):
                df.at[row_index, mealcalories] = 0
            if df.at[row_index, mealcalories] == 0:
                df.at[row_index, mealcalories] = calories
            else:
                print(f"The current value for {mealcalories} is {df.at[row_index, mealcalories]}")
                update_calories = input(f"Do you want to replace this value with {calories}? (y/n): ").lower()
                if update_calories == 'y':
                    df.at[row_index, mealcalories] = calories

        # Handle non-snack protein
        if mealprotein != "Snack Protein":
            if pd.isna(df.at[row_index, mealprotein]):
                df.at[row_index, mealprotein] = 0
            if df.at[row_index, mealprotein] == 0:
                df.at[row_index, mealprotein] = protein
            else:
                print(f"The current value for {mealprotein} is {df.at[row_index, mealprotein]}")
                update_protein = input(f"Do you want to replace this value with {protein}? (y/n): ").lower()
                if update_protein == 'y':
                    df.at[row_index, mealprotein] = protein

        return df

    def add_new_meal(self, df, date, mealcalories, mealprotein, calories, protein):
        # Add a new row to the df for the current days meal
        new_row = {
            'Date': date,
            mealcalories: calories,
            mealprotein: protein,
            'Total Calories': 0,
            'Total Protein': 0
        }

        new_row_df = pd.DataFrame([new_row])
        df = pd.concat([df, new_row_df], ignore_index=True)
        return df

    def recalculate_totals(self, df):
        # Recalculate total calories and protein for the day
        df['Total Calories'] = (
            df['Breakfast Calories'].fillna(0).astype(float) +
            df['Lunch Calories'].fillna(0).astype(float) +
            df['Dinner Calories'].fillna(0).astype(float) +
            df['Snack Calories'].fillna(0).astype(float)
        ).astype(int)  # Ensure the result is an integer

        df['Total Protein'] = (
            df['Breakfast Protein'].fillna(0).astype(float) +
            df['Lunch Protein'].fillna(0).astype(float) +
            df['Dinner Protein'].fillna(0).astype(float) +
            df['Snack Protein'].fillna(0).astype(float)
        ).astype(int)
        return df

    def delete_meal(self):
        df = self.file_manager.read_file()

        # Allow the user to select a date to delete the meal for
        while True:
            print('\nWhich Day would you like to select?')
            print('Enter 0 to return to main menu\n')
            for idx, date in enumerate(df['Date'].values, 1):
                print(f'Enter {idx} for {date}')

            try:
                userinput = int(input("Enter your choice: "))
                if 1 <= userinput <= len(df['Date'].values):
                    break
                elif userinput == 0:
                    return
                else:
                    os.system('cls||clear')
                    print("Invalid input. Please try again.")
            except ValueError:
                os.system('cls||clear')
                print("Invalid input. Please enter a number.")

        date_chosen = df['Date'].iloc[userinput - 1]
        row_index = df.index[df['Date'] == date_chosen].tolist()[0]

        # Prompt the user to select which meal field to delete
        fields = {
            '1': 'Breakfast Calories',
            '2': 'Breakfast Protein',
            '3': 'Lunch Calories',
            '4': 'Lunch Protein',
            '5': 'Dinner Calories',
            '6': 'Dinner Protein',
            '7': 'Snack Calories',
            '8': 'Snack Protein',
        }

        print('\nWhich Field Would you like to delete?\n')
        for key, field in fields.items():
            print(f'Enter {key} for {field}')

        while True:
            choice = input('Enter Choice: ')
            if choice in fields:
                self._set_field_to_nan(df, row_index, fields[choice])  # Set the chosen field to NaN
                break
            else:
                print("Invalid choice. Please try again.")

        df = self.recalculate_totals(df)  # Recalculate totals after deletion
        self.file_manager.write_file(df)

    def _set_field_to_nan(self, df, row_index, field_name):
        # Set the chosen field to NaN (effectively deleting the value)
        df.at[row_index, field_name] = pd.NA
        os.system('cls||clear')
        print(f"\n'{field_name}' set to NaN")

    def print_meal_history(self):
        df = self.file_manager.read_file()
        print(df)

        userinput = input('Enter anything to go back: ')

    def compare_goals(self):
        df = self.file_manager.read_file()
        self.recalculate_totals(df)

        # User chooses to compare calories or protein
        while True:
            print('Enter 0 to return')
            print("Enter 1 to compare Total Calories")
            print("Enter 2 to compare Total Protein")
            choice = input("Enter your choice: ")

            if choice in ['1', '2']:
                break