'''
Created on Jan 11, 2018

@author: shrikant_jagtap
'''

def calculateSquare(n):
    '''calling square method'''
    return n*n

numbers = [x for x in range(10)]
ls = list(map(calculateSquare, numbers))

print(ls)


''' lambda is most commonly used with map '''
ls = list(map(lambda x: x*x, numbers))
print("calculate squares using lambda :{}".format(ls))

''' addition of two list elements using map'''

list1 = [1,2,3,4,5]
list2 = [5,6,7,8,9]

result = list(map(lambda n1, n2:n1+n2, list1, list2))
''' Here map sending two elements from different list to lambda function and getting addition of them'''
 
print("addition of two list elements are:{}".format(result))

'''
    we can also map list of strings to int list
'''
string_list = ['1', '2', '3', '4', '5']
string_to_int = list(map(int, string_list))
print("map string to int {}".format(string_to_int))
