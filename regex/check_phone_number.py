'''
Created on Jan 5, 2018

@author: shrikant_jagtap
'''
import re

string = "The phone numbers are 666-454-4545 , 342-324-2342"
phone_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
matches = phone_regex.findall(string)
if matches:
    print("phone numbers are :",*matches)
else:
    print("No phone matches")
