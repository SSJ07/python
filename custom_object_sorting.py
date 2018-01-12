'''
Created on Jan 11, 2018

@author: shrikant_jagtap
'''
from operator import attrgetter


class Student(object):
    
    def __init__(self, roll_no, name):
        ''' This is constructor '''
        self.roll_no = roll_no
        self.name = name
        
    def __str__(self):
        return "roll_no={roll_no}, name={name}".format(roll_no=self.roll_no, name=self.name)

    def __repr__(self, *args, **kwargs):
        return "Student(roll_no={roll_no}, name={name})".format(roll_no=self.roll_no, name=self.name)
    
s = Student(1001, "Ganesh")
s1 = Student(1002, "Ajay")
s2 = Student(1003, "Sandya")
s3 = Student(1004, "Pooja")
s4 = Student(1005, "Rahul")

ls = []
ls.append(s2)
ls.append(s3)
ls.append(s)
ls.append(s1)
ls.append(s4)

print("\nbefore sorting list is:\n")
for i in ls:
    print(i)
    
ls.sort(key=attrgetter("name"), reverse=True)

print("\nAfter sorting list in descending order by name:\n")
for i in ls:
    print(i)
    
    
ls.sort(key=attrgetter("name"), reverse=False)

print("\nAfter sorting list in ascending order by name:\n")
for i in ls:
    print(i)

ls.sort(key=attrgetter("roll_no"), reverse=False)

print("\nAfter sorting list in ascending order by roll_no :\n")
for i in ls:
    print(i)
