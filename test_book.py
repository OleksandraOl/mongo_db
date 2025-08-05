from book import Book
from atlas_client import AtlasClient



new_connection = AtlasClient()
collection = new_connection.get_collection()

def test_book_instantiation():
    new_book = Book("To Kill a Mockingbird", "classic", ["Harper Lee"])

    assert new_book.title == "To Kill A Mockingbird"
    assert new_book.genre == "classic"
    assert new_book.authors == ["Harper Lee"]

def test_book_instantiation_author_not_mentioned():
    new_book = Book("To Kill a Mockingbird", "classic",)

    assert new_book.title == "To Kill A Mockingbird"
    assert new_book.genre == "classic"
    assert new_book.authors == []

def test_book_instantiation_upper_and_lowercase():
    new_book = Book("The CATcher in the rye", "COMING-of-age", ["J.D. salinger"])

    assert new_book.title == "The Catcher In The Rye"
    assert new_book.genre == "coming-of-age"
    assert new_book.authors == ["J.D. Salinger"]


def test_save_book():
    new_book = Book("Dune", "science fiction", ["Frank Herbert", ])

    assert collection.find_one({"title": "Dune"}) is None

    new_book.save(collection)

    assert len(collection.find_one({"title": "Dune"})) > 0

    # delete test cases
    collection.delete_many({"title": "Dune"})
    assert collection.find_one({"title": "Dune"}) is None
