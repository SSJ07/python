'''
Created on Jan 11, 2018

@author: shrikant_jagtap
'''

'''
    all function is total opposite of any function.
    all function takes iterable as parameter.
    It returns True if all elements are True in given iterables.
    It returns False if any single value is False.
'''

print("is all values are true? : {}".format(all(range(10))))
print("is all values are true? : {}".format(all(range(1,10))))
print("is all values are true? : {}".format(all([False, 1,2,34])))
print("is all values are true? : {}".format(all([True]*5)))

'''
    It wil produce output as :
    
    is all values are true? : False  @ Cause it contains 0
    is all values are true? : True   @ It contains non-zero values
    is all values are true? : False  @ It contains single False
    is all values are true? : True   @ It has all True values
'''
    
