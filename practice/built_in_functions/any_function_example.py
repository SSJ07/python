'''
Created on Jan 11, 2018

@author: shrikant_jagtap
'''

'''
    any function return True or False.  
    It takes iterable, string, dictionary as parameter
    It return True if any single value except 0 is available.
    It return False if list/iterable is empty of False is present in iterable not single True.
'''

print(any(range(10)))

ls  = []
print("any value is availble : {}".format(any(ls)))

ls = [0, False]

print(any(ls))

ls = [False] * 5 ## It create list with 5 False values
print(any(ls))
