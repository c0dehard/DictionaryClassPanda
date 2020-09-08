class book:

    def __init__(self, title, author):
        ''' This will create an ordinary book
        with Bookname.__init__() you can delete all entries of a book
        '''
        self.author = author
        self.title = title

    def __repr__(self):
        return self.title

    def information_receive(self, book):
        ''' Returns book title and author formatted
        :return:'''
        return "{self.title} written by {self.author}"


class library_book(book):
    def __init__(self, title, author, available):
        '''books for a library, can also have their own title / cover
        param title:
        :param author:
        :param available:'''
        super().__init__(title, author)
        self._available = available

    def information_receive(self):
        '''
        Shows how often a book title of a library book is still in stock (in stock)
        : return: '''
        super().information_receive()
        print(f"of {self.title} are still {self.title} available")


class bookstore(library_book):
    def __init__(self):
        '''A bookstore can only contain library books in this case.'''
        self.buecher = []

    def book_with_position(self, index): return self.buecher[index]

    def newBook(self, library_book):
        '''Add a book to the library
        Transfer TODO book lists directly
        : param book:
        : return:'''
        self.buecher.append(library_book)


def hint():
    print("""This module must be imported! Not directly executable.
    \next an example:
    a = library_book("Hairy Otter", "Jay.Kay. Blank",True)
    city_bookstore = bookstore()
    city_bookstore.newBook(a)
    print(city_bookstore.book_with_position(0))

    """)


if __name__ == "__main__":
    lb = library_book("Hairy Otta", "Jay.Kay. blank", True)
    city_bookstore = bookstore()
    city_bookstore.newBook(lb)
    print(city_bookstore.book_with_position(0))
