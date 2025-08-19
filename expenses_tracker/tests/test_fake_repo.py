from fake_repo import FakeRepo
from datetime import datetime


def test_add_expense():
    fake_repo = FakeRepo()

    fake_repo.add_expenses("fun", 10, "went to waterpark with friends",
                           datetime.strptime("2025-08-15", "%Y-%m-%d"))
    matches = [d for d in fake_repo.expenses_collection if
               d["category"] == "fun" and d["amount"] == 10]

    assert len(matches) == 1


def test_show_total_expenses_amount_for():
    fake_repo = FakeRepo()
    fake_repo.add_expenses(
        "food", 15, "lunch at new cafe",
        datetime.strptime("2025-08-16", "%Y-%m-%d")
    )
    fake_repo.add_expenses(
        "transport", 5, "bus ride to downtown",
        datetime.strptime("1800-08-17", "%Y-%m-%d")
    )

    total_amount = fake_repo.show_total_expenses_amount_for(datetime.strptime("1800-08-17", "%Y-%m-%d"), datetime.strptime("1800-08-17", "%Y-%m-%d") )

    assert total_amount == 5


def test_group_by_expenses():
    fake_repo = FakeRepo()

    fake_repo.add_expenses(
        "fun", 20, "movie night with friends",
        datetime.strptime("2025-08-18", "%Y-%m-%d")
    )

    fake_repo.add_expenses(
        "food", 8, "coffee and snack",
        datetime.strptime("2025-08-18", "%Y-%m-%d")
    )

    fake_repo.add_expenses(
        "food", 12, "dinner at Italian restaurant",
        datetime.strptime("2025-08-19", "%Y-%m-%d")
    )

    assert len(fake_repo.group_by("category")) != 0
    assert len(fake_repo.group_by("amount")) != 0

    print(fake_repo.group_by("category"))


def test_delete_expense():
    fake_repo = FakeRepo()

    fake_repo.add_expenses(
        "fun", 20, "movie night with friends",
        datetime.strptime("2025-08-18", "%Y-%m-%d")
    )

    fake_repo.add_expenses(
        "food", 8, "coffee and snack",
        datetime.strptime("2025-08-18", "%Y-%m-%d")
    )

    fake_repo.add_expenses(
        "food", 12, "dinner at Italian restaurant",
        datetime.strptime("2025-08-19", "%Y-%m-%d")
    )

    fake_repo.delete_expense(1)

    matches = [d for d in fake_repo.expenses_collection if
               d["category"] == "food" and d["description"] == "coffee and snack" and "amount" == 8]

    assert len(matches) == 0


def test_delete_all_expenses_for_time():
    fake_repo = FakeRepo()

    fake_repo.add_expenses(
        "fun", 20, "movie night with friends",
        datetime.strptime("2025-08-18", "%Y-%m-%d")
    )

    fake_repo.add_expenses(
        "food", 8, "coffee and snack",
        datetime.strptime("2025-08-19", "%Y-%m-%d")
    )

    fake_repo.add_expenses(
        "transport", 5, "bus ride to downtown",
        datetime.strptime("2025-08-10", "%Y-%m-%d")
    )

    fake_repo.add_expenses(
        "food", 12, "dinner at Italian restaurant",
        datetime.strptime("2025-08-25", "%Y-%m-%d")
    )

    fake_repo.delete_all_expenses_for_time(datetime.strptime("2025-08-18", "%Y-%m-%d"), datetime.strptime("2025-08-19", "%Y-%m-%d"))

    assert len(fake_repo.expenses_collection) == 2

