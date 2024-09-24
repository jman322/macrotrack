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
        
        df = self.recalculate_totals(df)    
        self.file_manager.write_file(df)  


    def get_user_input(self, field_name):
        while True:
            value = input(f'Enter {field_name}: ')
            try:
                return int(value)
            except ValueError:
                print(f"Please input a valid number for {field_name}")

    def update_meal(self, df, row_index, mealcalories, mealprotein, calories, protein):
        if mealcalories == "Snack Calories":
            if pd.isna(df.at[row_index, mealcalories]):
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

        if mealprotein == "Snack Protein":
            if pd.isna(df.at[row_index, mealprotein]):
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