'''
Created on Jan 11, 2018

@author: shrikant_jagtap
'''


class Student(object):
    
    def __init__(self, roll_no, name):
        ''' This is constructor '''
        self.roll_no = roll_no
        self.name = name
        
    def __str__(self):
        return "roll_no={roll_no}, name={name}".format(roll_no=self.roll_no, name=self.name)
    

stud = Student(100, "Shri")
print(stud)
