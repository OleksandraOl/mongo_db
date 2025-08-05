class Book:
    def __init__(self, title, genre, authors = None, ):
        self.title = title.title()
        self.genre = genre.lower()
        self.authors = authors or []

        self.authors = [author.title() for author in self.authors]


    def save(self, collection):
        collection.insert_one({
            "title": self.title,
            "genre": self.genre,
            "author/s": self.authors
        })
