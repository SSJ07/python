'''
Created on Jan 12, 2018

@author: shrikant_jagtap
'''

'''
    eval(expression)
    It takes string expression as parameter and evaluates it.
    And return it's result
'''
x = "10 + 20"
print("result of {} is :{}".format(x, eval(x))) 

expression = "print(10+20)"
eval(expression)

expression = "[x for x in range(10)]"
ls = eval(expression)
print("list of values by using eval is :{}".format(ls))

expression = "lambda x: x*x"
square  = eval(expression)
print(square(10))
