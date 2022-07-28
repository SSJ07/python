
'''
    we can pass parameters to decorators
'''

def header(numberOfStar, title=None, message=None):
    def decorate(func):
        def wrapper(*args, **kwargs):
            print("*" * numberOfStar)
            if title is not None:
                print(title)
            print("*" * numberOfStar)
            return func(*args, **kwargs)
        return wrapper
    return decorate


@header(50, "Python Decorators")
def printTitle(title):
    print("This is main title : {}".format(title))

printTitle("Welcome to Python Decorators")
