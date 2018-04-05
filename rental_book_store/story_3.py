'''
Created on Apr 6, 2018

@author: Shri
'''

from datetime import datetime
from models import Book

''' class for rental book store functionality '''
class RentalBookStore(object):
    
    ''' constructor '''
    def __init__(self):
        self.register = {}
        self.books = [Book(1, "Java", "regular"), Book(2, "A", "regular"),
                      Book(3, "last moment", "fiction"), Book(4, "Life", "Novel") 
                      ]
    
    ''' search particular book in books '''
    def search_book(self, book_name):
        for book in self.books:
            if book.get_name().lower() == book_name.lower():
                return book
        return None
    
    ''' rent particular book to customer '''
    def rent_book(self, cust_id, book_name, book_issued_date):
        book = self.search_book(book_name)
        if book is not None:
            if cust_id not in self.register:
                self.register[cust_id] = {book_issued_date:[book]}
            else:
                cust_data = self.register.get(cust_id)
                if book_issued_date in cust_data:
                    cust_data.get(book_issued_date).append(book)
                else:
                    cust_data[book_issued_date] = [book]
                self.register[cust_id] = cust_data
        else:
            print("Book is not available")
     
    ''' charges as per third story '''
    def get_book_dues(self, days, book_type):
        if book_type.lower() == 'fiction':
            return 4.5 if days < 3 else (days*3)
        else:
            return 2 if days<=2 else (((days-2)*1.5) + 2)
        
    ''' display customer details '''
    def display_customer_record(self, cust_id):
        customer_details = self.register.get(cust_id)
        print("\n***************  Customer {} rental book details are *********************".format(cust_id))
        if customer_details is None:
            print("No record found for customer {}".format(cust_id))
        else:
            for issued_date, books in customer_details.items():
                print(" issued date :{}  and books are :{}".format(issued_date, [book.get_name() for book in books]))
    
    ''' Calculate all dues of given customer '''
    def calculate_dues(self, cust_id):
        customer_details = self.register.get(cust_id)
        if customer_details is None:
            print("No record found for customer {}".format(cust_id))
        else:
            total_dues = 0
            print("***************  customer details for id {} *************".format(cust_id))
            for issued_date, books in customer_details.items():
                for book in books:
                    total_days = (datetime.now() - issued_date).days
                    charges = self.get_book_dues(total_days, book.get_type())
                    print("'{}' book '{}' type is rented from last {} days and charge is :{} Rs".format(book.get_name().upper(), book.get_type().upper(), total_days, charges))
                    total_dues+=charges
            print("=====Total is: {} Rs".format(total_dues))
    
    ''' Convert string date into datetime object '''                
    def get_date_obj(self, string_date):
        return datetime.strptime(string_date, "%Y%m%d")
    
import unittest
class BookStoreUnitTest(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        super(BookStoreUnitTest, self).__init__(*args, **kwargs)
        self.book_store = RentalBookStore()
        self.book_store.rent_book(1001, "Java", self.book_store.get_date_obj("20180401"))
        self.book_store.rent_book(1001, "last moment", self.book_store.get_date_obj("20180402"))
        self.book_store.rent_book(1001, "Life", self.book_store.get_date_obj("20180401"))
        
    def test_rent_book(self):
        self.book_store.rent_book(1002, "Java", self.book_store.get_date_obj("20180401"))
        self.book_store.rent_book(1002, "last moment", self.book_store.get_date_obj("20180402"))
        self.book_store.rent_book(1002, "Life", self.book_store.get_date_obj("20180401"))
    
    def test_display_customer_record(self):
        self.book_store.display_customer_record(1001)
        
    def test_calculate_dues(self):
        self.book_store.calculate_dues(1001)
        
        
if __name__ == '__main__':
    unittest.main()
