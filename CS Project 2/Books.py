class Book():
    def __init__(self, **kwargs):
        self.__title = kwargs["book_title"] if "book_title" in kwargs else "Unknown Book"

    def properties(self):
        print(self.__dict__)

    def get_title(self):
        return self.__title


class Encyclopedia(Book):
    def __init__(self):
        self.data = []



book_1 = Book(book_title= "Going Postal")
print(book_1.get_title())