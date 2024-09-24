class Calculator:
    def __init__(self, weight, height, age, gender):
        self.weight = weight
        self.height = height
        self.age = age
        self.gender = gender
        
    def calculate_tdee(self):
        if self.gender == 1:
            BMR = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
        elif self.gender == 2: 
            BMR = 10 * self.weight + 6.25 * self.height - 5 * self.age - 161
        else:
            print("Invalid gender choice, defaulting to male.")
            BMR = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
            
        activity_level = self.get_activity_level()
        
        if activity_level == 1:
            TDEE = BMR * 1.2
        elif activity_level == 2:
            TDEE = BMR * 1.375
        elif activity_level == 3:
            TDEE = BMR * 1.55
        elif activity_level == 4:
            TDEE = BMR * 1.725
        elif activity_level == 5:
            TDEE = BMR * 1.9
        else:
            print("Invalid choice, using Sedentary as default.")
            TDEE = BMR * 1.2
            
        return TDEE
        
    def get_activity_level(self):
        print('\nEnter Activity Level\n')
        print('Enter 1 for Sedentary: Little to no exercise')
        print('Enter 2 for Light: Light exercise 1-3 times a week')
        print('Enter 3 for Moderate: Moderate exercise 4-5 times a week')
        print('Enter 4 for Active: Daily exercise or intense workouts 3+')
        print('Enter 5 for Very Active: Intense exercise 6-7 times a week or very physically demanding job')
        while True:
            try:
                choice = int(input('Enter Choice: '))
                if choice not in [1,2,3,4,5]:
                    raise ValueError
                else:
                    return choice
            except ValueError:
                print('Invalid Input. Please input valid number')
                
    
    def display_tdee_results(self, TDEE):
        print(f"\nYour Total Daily Energy Expenditure (TDEE) is: {TDEE:.0f} calories/day\n")
        print(f"For mild weight loss (0.25kg/week) consume {0.9 * TDEE:.0f} calories/day")
        print(f"For weight loss (0.5kg/week) consume {0.79 * TDEE:.0f} calories/day")
        print(f"For mild weight gain (0.25kg/week) consume {1.1 * TDEE:.0f} calories/day")
        print(f"For weight gain (0.5kg/week) consume {1.21 * TDEE:.0f} calories/day")
        print(f"For fast weight gain (1kg/week) consume {1.41 * TDEE:.0f} calories/day")
    
    @staticmethod
    def calculate_protein(bodyweight):
        target_protein = bodyweight * 1.8
        print(f"Target protein intake: {target_protein:.1f}g of protein per day.")