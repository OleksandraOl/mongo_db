from collections import defaultdict
from bson import ObjectId

class ExpensesRepo:

    def __init__(self, collection):
        self.collection = collection

    def add_expenses(self, category, amount, description, datetime_):
        return self.collection.insert_one(
            {"category": category, "amount": amount, "description": description, "date": datetime_}
        )

    def show_total_expenses_amount_for(self, start_date, end_date):
        total_amount = 0
        for expense in self.collection.find({"date": {"$gte": start_date, "$lte": end_date}}):
            total_amount += expense["amount"]

        return total_amount

    def group_by(self, field_to_group_by: str):
        grouped_result = defaultdict(list)

        for expense in self.collection.find():
            grouped_result[expense[field_to_group_by]].append(expense)

        return grouped_result


    def delete_expense(self, input_id: str):
        return self.collection.delete_one({"_id": ObjectId(input_id)})


    def delete_all_expenses_for_time(self, start_date, end_date):
        return self.collection.delete_many({"date": {"$gte": start_date, "$lte": end_date}})
