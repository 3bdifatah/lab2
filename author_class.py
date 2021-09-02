#intiated class called Author with one argument and empty book list
class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

#function publish adds title of the book to the book list
    def pubish(self, title):
        self.books.append(title)

#displays the author and list of books
    def __str__(self):
        #if there is book joins them with comma seprating, else displays the message
        book_list = ', '.join(self.books) or 'No books in the list'
        print('___________________________________________________________')
        return f'Author Name: {self.name}\nBooks Published: {book_list}'

author1=Author('Al Sweigart')
author1.pubish('Automate The Boring Stuff With Python')
author1.pubish('Beyond The Basics Stuff With Python')
author1.pubish('Cracking Codes With Python')
print(author1)

author2=Author('abdifatah')
author2.pubish('abcs')
author2.pubish('123s')
print(author2)

author3=Author('Awali')
print(author3)