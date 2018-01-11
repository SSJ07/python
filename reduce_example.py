'''
Created on Jan 11, 2018

@author: shrikant_jagtap
'''

from functools import reduce

'''
    reduce function work like :
        suppose you have list [1,2,3,4]
        then fun(fun(fun(1,2),3),4)
'''

add_numbers = reduce(lambda x, y : x+y, range(1,11))

print("addition of 1 to 10 numbers are: {}".format(add_numbers))
''' Only for addition has alternative sum()'''
print("addition of 1 to 10 numbers are: {}".format(sum(list(range(1,11)))))

