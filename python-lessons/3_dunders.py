### Jack Maxon
# Jan 8,9 2024

"""
Notes on section 3 -- dunders.
"""

from functools import total_ordering

class Book:
    """
    Represents a book object.
    """
    def __init__(self, title: str, author: str, book_type: str, pages: int):
        self.title = title
        self.author = author
        self.book_type = book_type
        self.pages = pages

    def __repr__(self):
        return f"Attributes: {self.title}, {self.author}, {self.book_type}, {self.pages}."
    
    def __str__(self):
        return f"{self.title} by {self.author} in {self.book_type}."

    def __format__(self, format_spec: str):
        if format_spec == "short":
            return f"{self.title} - {self.author}."
        elif format_spec == "stealth":
            return f"A book containing exactly {self.pages}. Guess?"

        return repr(self)

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False 
        
        return self.title == other.title and self.author == other.author

    def __hash__(self):
        return hash((self.title, self.author))

    def __gt__(self,other):
        """
        Book A is greater than book B is pages(A) > pages(B)
        """
        if not isinstance(other, Book):
            return NotImplemented

        return self.pages > other.pages

    def __bool__(self):
        return bool(self.pages) and not(self.pages < 1)

    def __len__(self):
        return self.pages if self.pages > 0 else -self.pages

class BookShelf():
    def __init__(self, capacity):
        self.books = []
        self.capacity = capacity

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Only instances of Book can be added to the BookShelf")

        if not self.capacity > len(self.books):
            raise OverflowError("Bookshelf is full")    
        
        self.books.append(book)

    def __repr__(self):
        return str(self.books)

    def __add__(self, other: Book):
        if not isinstance(other, Book):
            raise TypeError("Only instances of Book may be added to BookShelf")

        new_shelf = BookShelf(self.capacity)
        for book in self.books:
            new_shelf.add_book(book)

        return new_shelf.add_book(other)

    def __radd__(self, other: Book):
        return self + other

    def __getitem__(self, item):
        if isinstance(item, str):
            return [book for book in self.books if item in book.title]

        return self.books[item]

class VideoNotes():
    """
    Notes and function/class calls from section 3.
    """

    b1 = Book("Antifragile", "Nassim Taleb", "Hardcover", 519)
    b2 = Book("America's Book", "Roger Lowenstein", "Paperback", 368)

    @staticmethod
    def vid1():
        """
        Covers dunder __repr__.
        """
        print(VideoNotes.b1) # __repr__ defines how this is displayed 
        print(VideoNotes.b2)

    @staticmethod
    def vid2():
        """
        Covers __str__. Should be able to eval(repr(b)) to create a new instance.
        """
        print(VideoNotes.b1) # __str__ -> informal for end user
        print(repr(VideoNotes.b1)) # __repr__ -> more dev/code user oriented

        # If possible, __repr__ should contain all the info necc. to recreate 
        # the instance

        print(VideoNotes.b1.__dict__)

    @staticmethod
    def vid3():
        """
        Covers __format__.
        """
        print(f"{100:.3f}") # 100 w/ 3 dp
        print(VideoNotes.b1)
        print(f"{VideoNotes.b1:short}")
        print(format(VideoNotes.b1, "stealth"))

    @staticmethod
    def vid4():
        """
        Covers __eq__.
        """
        print(VideoNotes.b1 == VideoNotes.b1) 
        # This statement prints False without __eq__ implementation
        # as the instances live at separate memory addresses 
        # (at least it would if we initialized them as separate objects)
        print(f"{id(VideoNotes.b1)}, {id(VideoNotes.b2)}") # memory addresses

    @staticmethod
    def vid5():
        """
        Covers __ne__ (not equal).
        """
        # don't define unless necessary 
        # ... inheritance of built-ints (?)
        # != is not (not __eq__) if there is a built in __ne__
        pass

    @staticmethod
    def vid6():
        """
        Hashing and mutability.
        """
        l = ["andy", 7]
        try:
            {
                l : "bek"
            }
        except TypeError:
            print("unhashable type")

        # a hashable object is:
        # comparable to other objects
        # if it compares ==, it shares a hash
        # hash value is invariant 
        name_str = "andy"
        name_str = "andy b" # str immutable 
        print(id(name_str)) # not same as before--old reference is removed by GC

    @staticmethod
    def vid7():
        """
        __hash__ dunder
        """
        # user defined classes are by default hashable until 
        # __eq__ is defined, then a __hash__ method needs to be defined
        b1 = VideoNotes.b1
        b1m = VideoNotes.b1
        print(hash(b1)); print(hash(b1m))
        print(id(b1)); print(id(b1m)) #lol

    @staticmethod
    def vid8():
        """
        __gt__, __lt__ (>, <), __le__, __ge__
        """
        print(VideoNotes.b1 > VideoNotes.b2)
        # Implementation of __eq__, __gt__, does not implement >=

    @staticmethod
    def vid9():
        """
        Functools. Provides total ordering by defining an __eq__ and inequality dunder.
        """
        # Book = total_ordering(Book)

    @staticmethod
    def vid10():
        """
        Truthiness __bool__
        """
        if VideoNotes.b1:
            print(True)
        else:
            print(False)

    @staticmethod
    def vid11():
        """
        __len__
        """
        # if __bool__ is not implemented, bool defaults to evaluating len

    @staticmethod
    def vid12():
        """
        Container class.
        """
        shelf = BookShelf(10)
        shelf.add_book(VideoNotes.b1)
        print(shelf)

    @staticmethod
    def vid13():
        """
        __add__, __radd__
        """
        shelf = BookShelf(10)
        shelf.add_book(VideoNotes.b1)
        print(shelf + VideoNotes.b2)
        print(shelf) # unchanged 
        print(VideoNotes.b2 + shelf) # not automatically commutative 

    @staticmethod
    def vid14():
        """
        __getitem__, special implementation for key searching . allows iteration 
        """
        shelf = BookShelf(10)
        shelf.add_book(VideoNotes.b1)
        print(shelf[0])

    @staticmethod
    def vid15():
        """
        Last video of section. 
        """
        print(BookShelf.__dict__)
        # bad practice to define own dunders 

if __name__ == '__main__':
    VideoNotes.vid15()