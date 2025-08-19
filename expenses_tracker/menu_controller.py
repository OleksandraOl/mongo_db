from datetime import datetime, timedelta

class MenuController:
    def __init__(self, expenses_repo):
        self.expenses_repo = expenses_repo

    def add_expense(self, category, amount, description):
        self.expenses_repo.add_expenses(category, amount, description, datetime_=datetime.now())


    def add_past_expense(self, category, amount, description, date):
        try:
            dt = datetime.strptime(date, "%Y-%m-%d")
            self.expenses_repo.add_expenses(category, amount, description, dt)
        except ValueError:
            print("Incorrect date format, should be YYYY-MM-DD")


    def total_expenses_week(self):
        curr_date = datetime.now()
        from_date = curr_date - timedelta(days=7)

        return self.expenses_repo.show_total_expenses_amount_for(from_date, curr_date)


    def group_expenses(self, option):
        option.lower()
        possible_options = ["category", "amount", "description", "date"]

        if option not in possible_options:
            print("Invalid option, choose from {}".format(possible_options))
            return None
        else:
            return self.expenses_repo.group_by(option)

    def delete_one_expense(self, num):
        self.expenses_repo.delete_expense(num)

    def delete_all_expenses_for_period(self, start_date, end_date):
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        self.expenses_repo.delete_all_expenses_for_time(start_date, end_date)

    @staticmethod
    def display_menu():
        print("\nChoose from the following options:")
        print("1. Create a new expense")
        print("2. Show week expenses amount")
        print("3. Display grouped expenses")
        print("4. Delete expense")
        print("9. Exit application")

    @staticmethod
    def get_valid_int(prompt="Please select a valid option: "):
        while True:
            try:
                user_input = int(input(prompt))
                return user_input  # valid input, return it
            except ValueError:
                print("Invalid input. Please choose from the available options.")
