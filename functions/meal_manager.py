from functions import file_manager
from datetime import datetime
import pandas as pd

class MealManager:
    def __init__(self, file_manager):
        self.file_manager = file_manager

    def add_meal(self, meal_type, mealcalories, mealprotein):
        self.file_manager.check_file()

        calories = self.get_user_input("Calories")
        protein = self.get_user_input("Protein")

        df = self.file_manager.read_file()

        todays_date = datetime.now().strftime('%Y-%m-%d')

        if 'Date' not in df.columns:
            df['Date'] = ""

        if todays_date in df['Date'].values:
            row_index = df.index[df['Date'] == todays_date].tolist()[0]
            self.update_meal(df, row_index, mealcalories, mealprotein, calories, protein)
        else:
            df = self.add_new_meal(df, todays_date, mealcalories, mealprotein, calories, protein)
            
            
        df = self.recalculate_totals(df, row_index)

        self.file_manager.write_file(df)
    def get_user_input(self, field_name):
        while True:
            value = input(f'Enter {field_name}: ')
            try:
                return int(value)
            except ValueError:
                print(f"Please input a valid number for {field_name}")

    def update_meal(self, df, row_index, mealcalories, mealprotein, calories, protein):
        """Updates an existing meal entry after confirming with the user."""


       
        if mealcalories == "Snack Calories":
            if not pd.isna(df.at[row_index, mealcalories]):
                print(f"The current value for {mealcalories} is {df.at[row_index, mealcalories]}")
                snack_option = input(f"Do you want to replace this value or add to it? (r = replace / a = add): ").lower()
                if snack_option == 'r':
                    df.at[row_index, mealcalories] = calories
                elif snack_option == 'a':
                    df.at[row_index, mealcalories] += calories
                else:
                    print("Invalid option. No changes made to Snack Calories.")
            else:
                df.at[row_index, mealcalories] = calories

    
        if mealprotein == "Snack Protein":
            if not pd.isna(df.at[row_index, mealprotein]):
                print(f"The current value for {mealprotein} is {df.at[row_index, mealprotein]}")
                snack_option = input(f"Do you want to replace this value or add to it? (r = replace / a = add): ").lower()
                if snack_option == 'r':
                    df.at[row_index, mealprotein] = protein
                elif snack_option == 'a':
                    df.at[row_index, mealprotein] += protein
                else:
                    print("Invalid option. No changes made to Snack Protein.")
            else:
                df.at[row_index, mealprotein] = protein

    
        if mealcalories != "Snack Calories":
            if not pd.isna(df.at[row_index, mealcalories]):
                print(f"The current value for {mealcalories} is {df.at[row_index, mealcalories]}")
                update_calories = input(f"Do you want to replace this value with {calories}? (y/n): ").lower()
                if update_calories == 'y':
                    df.at[row_index, mealcalories] = calories

        if mealprotein != "Snack Protein":
            if not pd.isna(df.at[row_index, mealprotein]):
                print(f"The current value for {mealprotein} is {df.at[row_index, mealprotein]}")
                update_protein = input(f"Do you want to replace this value with {protein}? (y/n): ").lower()
                if update_protein == 'y':
                    df.at[row_index, mealprotein] = protein


    def add_new_meal(self, df, date, mealcalories, mealprotein, calories, protein):
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
    def recalculate_totals(self, df, row_index):
        total_calories = (
            df.at[row_index, 'Breakfast Calories'] +
            df.at[row_index, 'Lunch Calories'] +
            df.at[row_index, 'Dinner Calories'] +
            df.at[row_index, 'Snack Calories']
        )

        total_protein = (
            df.at[row_index, 'Breakfast Protein'] +
            df.at[row_index, 'Lunch Protein'] +
            df.at[row_index, 'Dinner Protein'] +
            df.at[row_index, 'Snack Protein']
        )

        df.at[row_index, 'Total Calories'] = total_calories
        df.at[row_index, 'Total Protein'] = total_protein