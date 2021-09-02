#intiated class called Author with one argument and empty book list
class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

#function publish adds title of the book to the book list
    def publish(self, title):
        if title in self.books:
            print(f'{title} by {self.name} already in list {self.books}')           
        else:
            self.books.append(title)

#displays the author and list of books
    def __str__(self):
        #if there is book joins them with comma seprating, else displays the message
        print('___________________________________________________________')
        book_list = ', '.join(self.books) or 'No books in the list'
        return f'Author Name: {self.name}\nBooks Published: {book_list}'

author1=Author('Al Sweigart')
author1.publish('Automate The Boring Stuff With Python')
author1.publish('Beyond The Basics Stuff With Python')
author1.publish('Cracking Codes With Python')



author2=Author('abdifatah')
author2.publish('abcs')
author2.publish('123s')
author2.publish('123s')
author2.publish('abcs')

author3=Author('Awali')

print(author1)
print(author2)
print(author3)
