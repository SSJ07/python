'''
Created on Jan 11, 2018

@author: shrikant_jagtap
'''

''' lambda is anonymous function .
    It's one liner function 
'''

sqr = lambda x:x*x


print("square of 10 :{}".format(sqr(10)))

even_number = lambda x: [a for a in x if a%2==0]

x = [x for x in range(21)]
print("even numbers from 1 to 20 are: {}".format(even_number(x)))


add = lambda x, y: x+y

print("addition of {}+{}={}".format(10,20, add(10,20)))
