from book import Book
from bson import ObjectId

class BooksRepository:
    def __init__(self, collection):
        self.collection = collection

    def add_book(self, book: Book):
        new_book_dict = {
            "title": book.title,
            "genre": book.genre,
            "author/s": book.authors
        }

        try:
            insert_action = self.collection.insert_one(new_book_dict)
            # returns True if successful
            return insert_action.acknowledged
        except Exception as e:
            print(f"Insert error: {e}")
            # returns False if any other issue occurred
            return False


    def update_book(self, book_id, updated_info):
        # check if the input data is valid
        self.is_valid_data(updated_info)

        try:
            result = self.collection.update_one(
            {"_id": ObjectId(book_id)},
            {"$set": updated_info}
        )
            modified_documents = result.modified_count
            # print statement for the debugging process
            print(f"Modified: {modified_documents}")
            return modified_documents
        except Exception as e:
            print(f"Update error: {e}")
            return 0

    def find_book_by_title(self, input_title):
        try:
            return list(self.collection.find({"title": input_title.title()}))
        except Exception as e:
            print(f"Encountered error: {e}")
            return []

    def find_book_by_author(self, author_name):
        try:
            return list(self.collection.find({"author/s": author_name.title()}))
        except Exception as e:
            print(f"Encountered error: {e}")
            return []

    def delete_book(self, book_id):
        try:
            result = self.collection.delete_one({"_id": ObjectId(book_id)})
            deleted_documents = result.deleted_count
            # print statement for the debugging process
            print(f"Documents deleted: {deleted_documents}")
            return deleted_documents
        except Exception as e:
            print(f"Deletion error: {e}")
            return 0

    def delete_all_books_matched(self, filter_parameters):
        self.is_valid_data(filter_parameters)

        try:
            result = self.collection.delete_many(filter_parameters)
            deleted_documents = result.deleted_count
            # print statement for the debugging process
            print(f"Documents deleted: {deleted_documents}")
            return deleted_documents
        except Exception as e:
            print(f"Deletion error: {e}")
            return 0


    @staticmethod
    # check if the input data is valid or raises proper exceptions
    def is_valid_data(data):
        if data is None:
            raise ValueError("Input data must not be None.")

        if not isinstance(data, dict):
            raise TypeError("Input data must be a dictionary.")

        if len(data) == 0:
            raise ValueError("Input data cannot be empty.")

        return True