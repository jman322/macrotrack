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
    
    def delete_meal(self):
        df = self.file_manager.read_file()

        print('\nWhich Day would you like to select?\n')
        for idx, date in enumerate(df['Date'].values, 1):
            print(f'Enter {idx} for {date}')

        userinput = int(input("Enter your choice: "))
        if userinput < 1 or userinput > len(df['Date'].values):
            print("Invalid input. Please try again.")
            return

        date_chosen = df['Date'].iloc[userinput - 1]
        row_index = df.index[df['Date'] == date_chosen].tolist()[0]

       
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

        choice = input('Enter Choice: ')
        if choice in fields:
            self._set_field_to_nan(df, row_index, fields[choice])
        else:
            print("Invalid choice.")

        df = self.recalculate_totals(df)
        self.file_manager.write_file(df)

    def _set_field_to_nan(self, df, row_index, field_name):
        df.at[row_index, field_name] = pd.NA 
        print(f"\n'{field_name}' set to NaN")
        
    def print_meal_history(self):
        df = self.file_manager.read_file()
        print(df)
        
        userinput = input('Enter 0 to go back: ')
        if userinput != '0':
            print('\nInvalid Input\n')
            self.print_meal_history()
            
    def compare_goals(self):
        df = self.file_manager.read_file()  # Read data from CSV using FileManager
        self.recalculate_totals(df)

        print("Enter 1 to compare Total Calories")
        print("Enter 2 to compare Total Protein")
        choice = input("Enter your choice: ")

        if choice not in ['1', '2']:
            print("Invalid choice. Returning to menu.")
            return

        try:
            user_goal = int(input("Enter your target value to compare: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return

        if choice == '1':
            self.compare_metric(df, 'Total Calories', user_goal)
        elif choice == '2':
            self.compare_metric(df, 'Total Protein', user_goal)
            
    def compare_metric(self, df, metric, user_goal):
        print(f"\nComparing against {metric}")
        for index, row in df.iterrows():
            if row[metric] >= user_goal:
                print(f"{row['Date']}: {row[metric]} (met or exceeded target)")
            else:
                print(f"{row['Date']}: {row[metric]} (below target)")
        input('Enter anything to exit.')