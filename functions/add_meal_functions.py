import csv

def addmeal():
    with open('data/meals.csv', mode='w') as csvfile:
        fieldnames = ['Date', 'Breakfast Calories','Breakfast Protien','Lunch Calories','Lunch Protien','Dinner Calories','Dinner Protien','Snack Calories','Snack Protien','Total Caloriees', 'Total Protien']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'Breakfast Calories': 90, 'Breakfast Protien': 100})

        print('Which meal Would You like to add?')
        print('Enter 1 for Breakfast')
        print('Enter 2 for Lunch')
        print('Enter 3 for Dinner')
        print('Enter 4 for Snack')
        print('Enter 5 to go Back to Main Menu')
        
        choice = input("Enter your choice: ")

        while choice != "5":
            if choice == "1":
                Calories = input('Enter Calories: ')
                try:
                    int_value = int(Calories)
                except ValueError:
                    print("Please input a number.")
                Protien = input('Enter Protien: ')
                try:
                    int_value = int(Protien)
                except ValueError:
                    print("Please input a number.")
            if choice == "2":
                pass
            if choice == "3":
                pass            
            if choice == "4":
                pass
            if choice == "5":
                pass

addmeal()
