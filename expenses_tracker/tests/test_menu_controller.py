from fake_repo import FakeRepo
from menu_controller import MenuController
from datetime import datetime, timedelta
from fake_repo import FakeRepo

def test_add_expense_no_input_time_should_be_equal_to_current_day():
    fake_repo = FakeRepo()
    menu_controller = MenuController(fake_repo)

    menu_controller.add_expense("transport", 5, "bus ride to downtown")

    matches =  [d for d in menu_controller.expenses_repo.expenses_collection if
               d["description"] == "bus ride to downtown"]

    assert matches[0]["date"].day == datetime.today().day

def test_total_expense_week():
    fake_repo = FakeRepo()
    fake_repo.expenses_collection = [
        {
            "category": "fun",
            "amount": 20,
            "description": "movie night with friends",
            "date": datetime.now() - timedelta(days=7)
        },
        {
            "category": "food",
            "amount": 8,
            "description": "coffee and snack",
            "date": datetime.now() - timedelta(days=10)
        },
        {
            "category": "transport",
            "amount": 5,
            "description": "bus ride to downtown",
            "date": datetime.now()
        },
        {
            "category": "food",
            "amount": 12,
            "description": "dinner at Italian restaurant",
            "date": datetime.now() - timedelta(days=8)
        },
        {
            "category": "fun",
            "amount": 15,
            "description": "board game night",
            "date": datetime.now()
        },
        {
            "category": "transport",
            "amount": 7,
            "description": "taxi ride",
            "date": datetime.now()
        }
    ]

    menu_controller = MenuController(fake_repo)

    assert menu_controller.total_expenses_week() == 27
