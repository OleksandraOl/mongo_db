from atlas_client import AtlasClient
from expenses_repo import ExpensesRepo
from fake_repo import FakeRepo
from menu_controller import MenuController
import pyfiglet

# TODO: uncomment for an actual db connection
# new_connection = AtlasClient()
# curr_collection = new_connection.get_collection()

# TODO: replace with ExpensesRepo() and real db collection
fake_expense_repo = FakeRepo()
controller = MenuController(fake_expense_repo)


greeting = pyfiglet.figlet_format("Welcome to Expense Tracker", font="slant")
print(greeting)

while True:
    controller.display_menu()
    user_choice = controller.get_valid_int()

    if user_choice == 1:
        print("\nWould you like to add? ")
        print("1. Current expense")
        print("2. Past expense")

        expense = controller.get_valid_int()
        # TODO: need to add data validation
        if expense == 1:
            category, amount, description = input("Enter category, amount, description: ").split()
            try:
                controller.add_expense(category, int(amount), description)
                print("Successfully added new expense")
            except Exception as e:
                print(e)
                continue
        elif expense == 2:
            category, amount, description, date = input("Enter category, amount, description, date: ").split()
            try:
                controller.add_past_expense(category, int(amount), description, date)
                print("Successfully added new expense")
            except Exception as e:
                print(e)
                continue
    elif user_choice == 2:
        print("Total expenses: ", controller.total_expenses_week())
    elif user_choice == 3:
        group_category = input("Choose what you'd like to have it grouped by category/amount/description/date: ")
        print(controller.group_expenses(group_category))
    elif user_choice == 4:
        print("\nWould you like to delete...? ")
        print("1. One expense")
        print("2. Multiple expenses")

        delete_option = controller.get_valid_int()
        if delete_option == 1:
            # TODO: need to change int type to string type for real repo
            object_id = int(input("Please enter object id: "))
            try:
                controller.delete_one_expense(object_id)
                print("Successfully deleted expense")
            except Exception as e:
                print(e)
                continue
        elif delete_option == 2:
            # TODO: needs to handle incorrect date format
            start_date = input("Please enter start date: 'YY-MM-DD': ")
            end_date = input("Please enter end date: 'YY-MM-DD': ")
            try:
                controller.delete_all_expenses_for_period(start_date, end_date)
                print("Successfully deleted chosen expenses")
            except Exception as e:
                print(e)
                continue
    elif user_choice == 9:
        print("Thank you for using application. Have a great day!")
        break
    else:
        print("Please choose a valid option")


