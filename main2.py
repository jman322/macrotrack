from functions.menu import Menu
from functions.funcs import addmeal, addmacro, addsnack, create_menu, delmeal, printdf, calcalc, procalc, comparegoals, save_and_exit

menu_options = {
    1: ("Add Meal", addmeal),
    2: ("Delete Meal", delmeal),
    3: ("List Meal History", printdf),
    4: ("Calculate Target Calories", calcalc),
    5: ("Calculate Target Protein", procalc),
    6: ("View Progress", comparegoals),
    7: ("Save and Exit", save_and_exit)
}
menu = Menu(menu_options)

menu.display()

user_choice = menu.get_user_choice()
print(f"You selected: {user_choice}")