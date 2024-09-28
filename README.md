# Macrotrack

## Overview

Macrotrack allows users to track their daily meals macros and calculate their Total Daily Energy Expenditure (TDEE) and target protein intake needed for muscle growth. It provides the user withfunctionality for adding, deleting, and viewing meal data stored in a CSV file. Users can also compare their calorie and protein intake with preset goals.

## Features

- Add Meal: Add meals to a csv file where you can log you daily breakfast, lunch, dinner and snacks Calories and Protien.

- Delete Meal: Ability to delete any meal from any day in the csv.

- List Meal History: Print the csv in the console, or alternatively you can find the meals.csv in the data file and view it in any csv viewer.

- Calorie Calculator: Uses the Mifflin-St Jeor Method to calculate your Basal Metabolic Rate (BMR), which is then used to calculate your Total Daily Calorie Expenditure (TDEE), multiplied by your chosen exercise level. This is a scientifically proven method and one of the most accurate ways to calculate weight loss, gain, and calorie goals.

- Protein Calculator: Uses your body weight and multiplies it by 1.8 to get the target amount of protein you.

## Requirements

The application requires Python 3 and the following third-party libraries:

- `pandas`
- `colorama`

### Installing Required Libraries

To install the required libraries, run the following command:

```bash
pip install pandas colorama
```
## System Requirements

 - OS: Linux, Windows or MacOS
 - Processor: 1GHz or faster
 - Memory: 512MB of RAM
 - Disk Space: 10MB of space for python 3 and csv data storage
 - Display: Terminal or CLI

## License

[MIT](MIT.txt)

[3rd Party Software](BSD3-Clause.txt)
