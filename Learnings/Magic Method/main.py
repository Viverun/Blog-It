#Dunder Methods = Dunder Methods(Double Underscore) __init__, __str__, __eq__,
#                 They are automatically called by many of Python's built-in operations.
#                 They allow developers to define or customize the behavior of objects
# class Student:
#     def __init__(self, name, gpa):
#         self.name = name
#         self.gpa = gpa
#     def __str__(self):
#         return f"Name: {self.name} GPA:{self.gpa}"
#     def __eq__(self, other):
#         return self.name == other.name
#     def __gt__(self, other):
#         return self.gpa > other.gpa
# student1= Student("Spongebob", 3.4)
# student2 = Student("Squidward", 3.3)
# print(student1)
# print(student1 == student2)
# print(student1 > student2)

class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
    def __str__(self):
        return f"{self.title} by {self.author}"
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    def __add__(self, other):
        return self.num_pages + other.num_pages
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    def __getitem__(self, item):
        if item == "title":
            return self.title
        elif item == "author":
            return self.author
        elif item == "num_pages":
            return self.num_pages
        else:
            return f"Key '{item}' was not found "


book1 = Book("Harry Potter","J.K Rowling",223 )
book2 = Book("The Hobbit", "J.R.R Tolkein", 320)
book3 = Book("The Hobbit", "J.R.R Tolkein", 320)
print(book2)
print(book3)
print(book2 == book3)
print(book1 < book2)
print(book1 > book2)
print(book1+book2)
print("Hary" in book1)
print(book1["title"])
print(book2["author"])
print(book1["num_pages"])
print(book1["numpages"])