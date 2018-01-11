'''
Created on Jan 11, 2018

@author: shrikant_jagtap
'''

'''
    filter function required function as first argument and iterable (list|set) as second 
    arguemnt. It's same as map but returns boolean instead of other value 
'''

numbers = [x for x in range(11)]

even_numbers = list(filter(lambda x: x%2 == 0, numbers))
print("even numbers are :{}".format(even_numbers))

odd_numbers = list(filter(lambda x: x%2 !=0, numbers))
print("odd numbers are :{}".format(odd_numbers))


ls = [1,2,3,4, 'hello', 'java', 'name', 6,7]
numbers_only = list(filter(lambda x: type(x)==int, ls))
print("numbers only :{}".format(numbers_only))
