# Simple Library System
#Using Gemini
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True  # Initially, the book is available

    def borrow(self):
        if self.is_available:
            self.is_available = False
            return True  # Borrow successful
        else:
            return False  # Book already borrowed

    def return_book(self):
        self.is_available = True

    def display_info(self):
        availability = "Available" if self.is_available else "Borrowed"
        print(f"Title: {self.title}, Author: {self.author}, Status: {availability}")

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = [] # List to track borrowed books.

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"Sorry, '{book.title}' is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} did not borrow '{book.title}'")

    def display_info(self):
        print(f"Member ID: {self.member_id}, Name: {self.name}")
        if self.borrowed_books:
            print("Borrowed Books:")
            for book in self.borrowed_books:
                print(f"- {book.title}")
        else:
            print("No books borrowed.")

# Example Usage:
book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams")
book2 = Book("Pride and Prejudice", "Jane Austen")

member1 = Member(101, "Alice")
member2 = Member(102, "Bob")

book1.display_info()
member1.display_info()

member1.borrow_book(book1)
member2.borrow_book(book1) #example of a failed borrow.
member1.borrow_book(book2)

book1.display_info()
member1.display_info()

member1.return_book(book1)

book1.display_info()
member1.display_info()