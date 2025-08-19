from collections import defaultdict

class FakeRepo:

    def __init__(self):
        self.expenses_collection = []


    def add_expenses(self, category, amount, description, datetime_):
        new_expense = {"category": category, "amount": amount, "description": description, "date": datetime_}
        self.expenses_collection.append(new_expense)

        return new_expense


    def show_total_expenses_amount_for(self, start_date, end_date):
        total_amount = 0
        for expense in self.expenses_collection:
            if start_date <= expense["date"] <= end_date:
                total_amount += expense["amount"]

        return total_amount


    def group_by(self, field_to_group_by):
        grouped_result = defaultdict(list)

        for expense in self.expenses_collection:
            grouped_result[expense[field_to_group_by]].append(expense)

        return grouped_result


    def delete_expense(self, input_position: int):
        del self.expenses_collection[input_position]

    def delete_all_expenses_for_time(self, start_date, end_date):

        for expense in self.expenses_collection[:]:
            if start_date <= expense["date"] <= end_date:
                self.expenses_collection.remove(expense)