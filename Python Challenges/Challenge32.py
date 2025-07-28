'''You are working on a project to develop a class representing a Book. The Book 
class should have properties such as title, author, and year of publication. 
Implement the constructor for the Book class that initializes these properties 
when a new Book object is created. Additionally, provide a method called 
getBookInfo() 
that returns a string with the book's details in the format "Title: 
[title], Author: [author], Year: [year]". 
Write the constructor and the getBookInfo()  
method for the Book class. '''

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def getBookInfo(self):
        return f"Title : {self.title}, Author : {self.author}, Year : {self.year}"

# Example usage
book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book2 = Book("CheGuvera", "Viladimar", 1972)
book3 = Book("Prabhakaran", "Bala singam", 2009)
print(book1.getBookInfo())
print(book2.getBookInfo())
print(book3.getBookInfo())
