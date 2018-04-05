'''
Created on Apr 6, 2018

@author: Shri
'''

class Book(object):
    
    def __init__(self, isbn_num, name, book_type):
        self.isbn_num = isbn_num
        self.name = name
        self.book_type = book_type
    
    def get_name(self):
        return self.name
    
    def get_type(self):
        return self.book_type
    
    def __str__(self):
        return "[" + str(self.isbn_num) + "," + self.name + ", " + self.book_type + "]";
    
