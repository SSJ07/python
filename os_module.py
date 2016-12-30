'''
    This program shows usage of os module
'''

import os

# use os.system() to execute linux commands

os.system("clear") #clears screen
os.system("pwd") # return present working dir

os.chdir("/home/shri/programming/Python") #changes current working dir

# os module has path submodule

print os.path.isdir("/home/shri/programming/Python")
print os.path.isfile("/home/shri/programming/Python/send_sms.py")
print os.path.join("/home/shri", "programming") # returns /home/shri/programming
print os.path.split("/home/shri/programming") # returns (/home/shri, programming)
print "isLink "+ str(os.path.islink("<a href=#> click here </a>"))
print "current working dir" + os.getcwd()

#get files from particular directory

for root, dr, files in os.walk("/home/shri/programming/Python"):
    for ffile in files:
        print ffile
