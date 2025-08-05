from books_repository import BooksRepository
from book import Book
from atlas_client import AtlasClient


new_connection = AtlasClient()
collection = new_connection.get_collection()
new_book_rep = BooksRepository(collection)

def test_add_book():
    new_book = Book("Brave New World", "science fiction", ["Aldous Huxley", "Ray Bradbury"])

    assert new_book_rep.add_book(new_book) is True


def test_update_book():
    new_book = Book("blabla", "romance", ["Somebody"])
    new_book_rep.add_book(new_book)

    book_to_update_later = collection.find_one({"title": "Blabla"})

    assert new_book_rep.update_book(book_to_update_later["_id"], {"title": "Something fancy"}) == 1


def test_find_book_by_title():
    new_book = Book("Some crazy title", "horror", ["Me", "My neighbour"])
    new_book_rep.add_book(new_book)

    assert len(new_book_rep.find_book_by_title("Some crazy title")) > 0


def test_find_book_by_author():
    new_book = Book("Even more crazier title", "sci-fi", ["Me", "My neighbour"])
    new_book_rep.add_book(new_book)

    assert len(new_book_rep.find_book_by_author("Me")) > 0


def test_delete_book():
    new_book = Book("Something new", "sci-fi", ["Me", "My neighbour"])
    new_book_rep.add_book(new_book)

    assert len(new_book_rep.find_book_by_title("Something new")) > 0
    added_book = collection.find_one({"title": "Something New"})
    book_id = added_book["_id"]
    str_id = str(book_id)
    assert new_book_rep.delete_book(str_id) == 1


def test_delete_all_books_matched():
    new_book1 = Book("Something new", "sci-fi", ["Me", "My neighbour"])
    new_book2 = Book("Something new", "horror", ["Me", "My neighbour"])

    new_book_rep.add_book(new_book1)
    new_book_rep.add_book(new_book2)

    new_book_rep.delete_all_books_matched({"title": "Something New"})

    assert collection.find_one({"title": "Something New"}) is None