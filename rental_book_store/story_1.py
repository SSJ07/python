'''
Created on Apr 6, 2018

@author: Shri
'''

from datetime import datetime
import unittest

''' class for rental book store functionality '''
class RentalBookStore(object):
    
    ''' constructor '''
    def __init__(self):
        self.register = {}
    
    ''' Give book to customer on rent basis'''
    def rent_book(self, cust_id, book_name, book_issued_date):
        if cust_id not in self.register:
            self.register[cust_id] = {book_issued_date:[book_name]}
        else:
            cust_data = self.register.get(cust_id)
            if book_issued_date in cust_data:
                cust_data.get(book_issued_date).append(book_name)
            else:
                cust_data[book_issued_date] = [book_name]
            self.register[cust_id] = cust_data
     
    ''' calculate dues of customer '''
    def calculate_dues(self, cust_id):
        customer_details = self.register.get(cust_id)
        if customer_details is None:
            print("No record found for customer {}".format(cust_id))
        else:
            total_dues = 0
            for issued_date, books in customer_details.items():
                for book in books:
                    days = (datetime.now() - issued_date).days
                    print("{} day {} book is holded".format(days, book))
                    total_dues += days
            print("Total dues amount of customer {} is : {} Rs".format(cust_id, total_dues))
            
    ''' convert string date into datetime object '''
    def get_date_obj(self, string_date):
        return datetime.strptime(string_date, "%Y%m%d")
    


''' Unit test case for RentalBookStore '''
class BookStoreUnitTest(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        super(BookStoreUnitTest, self).__init__(*args, **kwargs)
        self.book_store = RentalBookStore()
    
    def test_rent_book(self):
        self.book_store.rent_book(1001, "Java", self.book_store.get_date_obj("20180401"))
        self.book_store.rent_book(1001, "Python", self.book_store.get_date_obj("20180402"))
    
    def test_calculate_dues(self):
        self.book_store.rent_book(1001, "Java", self.book_store.get_date_obj("20180401"))
        self.book_store.rent_book(1001, "Python", self.book_store.get_date_obj("20180402"))
        self.book_store.calculate_dues(1001)
        
if __name__ == '__main__':
    unittest.main()
