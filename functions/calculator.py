class Calculator:
    def __init__(self, weight, height, age, gender):
        self.weight = weight  # users weight in kg
        self.height = height  # users height in cm
        self.age = age  # users age
        self.gender = gender  # users gender

    # calculate tdee based on weight, height, age, and gender
    def calculate_tdee(self):
        if self.gender == 1:  # male
            BMR = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
        elif self.gender == 2:  # female
            BMR = 10 * self.weight + 6.25 * self.height - 5 * self.age - 161
        else:
            print("invalid gender choice, defaulting to male")
            BMR = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5

        activity_level = self.get_activity_level()  # get activity level from user input

        # calculate tdee based on activity level
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
            print("invalid choice, using sedentary as default")
            TDEE = BMR * 1.2

        return TDEE

    # prompt the user to select activity level
    def get_activity_level(self):
        print('\nenter activity level\n')
        print('enter 1 for sedentary: little to no exercise')
        print('enter 2 for light: light exercise 1-3 times a week')
        print('enter 3 for moderate: moderate exercise 4-5 times a week')
        print('enter 4 for active: daily exercise or intense workouts 3+')
        print('enter 5 for very active: intense exercise 6-7 times a week or very physically demanding job')
        while True:
            try:
                choice = int(input('enter choice: '))
                if choice not in [1, 2, 3, 4, 5]:
                    raise ValueError
                else:
                    return choice
            except ValueError:
                print('invalid input. please input valid number')

    # display the tdee results and various recommendations
    def display_tdee_results(self, TDEE):
        print(f"\nyour total daily energy expenditure (tdee) is: {TDEE:.0f} calories/day\n")
        print(f"for mild weight loss (0.25kg/week) consume {0.9 * TDEE:.0f} calories/day")
        print(f"for weight loss (0.5kg/week) consume {0.79 * TDEE:.0f} calories/day")
        print(f"for mild weight gain (0.25kg/week) consume {1.1 * TDEE:.0f} calories/day")
        print(f"for weight gain (0.5kg/week) consume {1.21 * TDEE:.0f} calories/day")
        print(f"for fast weight gain (1kg/week) consume {1.41 * TDEE:.0f} calories/day")

    # static method to calculate target protein intake
    @staticmethod
    def calculate_protein(bodyweight):
        target_protein = bodyweight * 1.8  # recommended protein intake based on body weight
        print(f"target protein intake: {target_protein:.1f}g of protein per day")
