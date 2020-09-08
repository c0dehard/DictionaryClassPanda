import unittest


class book:

    def __init__(self, title, author):
        self.author = author
        self.title = title

    def __repr__(self):
        return self.title

    def full_info(self, book):
        return f"{self.title} written by {self.author}"


class sellable_book(book):
    def __init__(self, title, author, available, price):
        super().__init__(title, author)
        self._available = available
        self._price = price


class bookstore(sellable_book):
    def __init__(self):
        '''A bookstore can only contain library books in this case.'''
        self.bookshelf = []

    def book_with_position(self, index): return self.bookshelf[index]

    def add_book(self, sellable_book):
        '''Add a sellable_book to the library'''
        self.bookshelf.append(sellable_book)


def hint():
    print("""\033[93m
    This module must be imported! It's not directly executable.

    e.g.:

    \033[94m- Create a sellable book
    \033[95ma = sellable_book("Hairy Otter", "Jay.Kay. Rolling", True, 17.58)

    \033[94m- Create a bookstore
    \033[95mlocal_book_store = bookstore()

    \033[94m- Add book to library
    \033[95mlocal_book_store.add_book(a)

    \033[94m- Check what book in certain position is
    \033[95mprint(local_book_store.book_with_position(0))
    \033[0m
    """)


# Create a library book
a = sellable_book("Hairy Otter", "Jay.Kay. Rolling", True, 17.58)
# Create a bookstore
local_book_store = bookstore()
# Add book to library
local_book_store.add_book(a)


class test_book_module(unittest.TestCase):
    def test1(self):
        assert type(local_book_store.book_with_position(0)) == sellable_book
        self.assertEqual(
            # current value, expected value
            str(local_book_store.book_with_position(0)), "Hairy Otter")


if __name__ == "__main__":
    hint()
    unittest.main()
