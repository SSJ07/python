'''
Created on Jan 18, 2018

@author: shri
'''

'''
    vars() method takes maximum one argument.
    It returns value in dictionary format.
    It takes as argument like class, module, or any object having __dict__
    attribute.
'''

class Student(object):
    
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name

stud = Student(1001, "shri")

print("vars of stud object are :{}".format(vars(stud)))
print("type of vars return method is :{}".format(type(vars(stud))))
