from _datetime import datetime


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
        return "[" + str(self.isbn_num) + "," + self.name + ", " + self.type + "]";
    

class Customer(object):
    
    def __init__(self, cust_id, name):
        self.cust_id = cust_id
        self.name = name
    
    def get_cust_id(self):
        return self.cust_id
    
    def __str__(self):
        return "[" + str(self.cust_id) + ", " + self.name + "]"
    
class BookStore(object):
    
    def __init__(self):
        self.register = {}
        self.books = [Book(1, "Java", "Programming"), Book(2, "A", "Regular"),
                      Book(3, "last moment", "fiction"), Book(4, "Life", "Novel") 
                      ]
    
    def search_book(self, book_name):
        for book in self.books:
            if book.get_name().lower() == book_name.lower():
                book = self.books
                return book
        return None
    
    def rent_book(self, cust_id, book_name):
        book = self.search_book(book_name)
        if book is not None:
            if cust_id not in self.register:
                self.register[cust_id] = {datetime.now().date():[book]}
            else:
                cust_data = self.register.get(cust_id)
                today_date = datetime.now().date()
                if today_date in cust_data:
                    cust_data.get(today_date).append(book)
                else:
                    cust_data[today_date] = [book]
                self.register[cust_id] = cust_data
        else:
            print("Book is not available")
    
    def return_book(self, cust_id, book_name):
        pass
    
    def calculate_charges(self, customer):
        pass
    
if __name__ == '__main__':
    bookStore = BookStore()
    bookStore.rent_book(1001, "Java")
    bookStore.rent_book(1001, "A")
    bookStore.rent_book(1002, "A")
    print(bookStore.register)
