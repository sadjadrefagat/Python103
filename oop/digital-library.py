class Book:
    def __init__(self, name, isbn, publisher, author, topic):
        self.name = name
        self.isbn = isbn
        self.publisher = publisher
        self.author = author
        self.topic = topic

    def __str__(self):
        return f'Name: {self.name}\nISBN: {self.isbn}\nPublished by: {self.publisher}'


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if self.search_by_isbn(book.isbn) == None:
            self.books.append(book)
        else:
            print('Duplicate book!')

    def print_all(self):
        print(f'There is {len(self.books)} books in library:')
        for book in self.books:
            print('-' * 30)
            print(book)

    def search_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def search_by_name(self, name):
        result = []
        for book in self.books:
            if book.name.find(name) != -1:
                result.append(book)
        return result


lib = Library()
lib.add_book(Book(name='C++ in 21 days',
                  isbn='1001',
                  publisher='sref.ir',
                  author='Sadjad Refagat',
                  topic='Programming'))
lib.add_book(Book(name='Python in 21 days',
                  isbn='1002',
                  publisher='sref.ir',
                  author='Sadjad Refagat',
                  topic='Programming'))
lib.print_all()
books = lib.search_by_name('21 days')
if books:
    for book in books:
        print(book)
else:
    print('Not found!')