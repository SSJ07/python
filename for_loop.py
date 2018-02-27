## for loop in python
## implemented under python 2.x
## in python 3.x use print function as print("string") 
for i in range(10):
	print i, " ", 

print "\nprint value 10 to 100 increment by 5"

for i in range(10, 100, 5):
	print i, " ", 


print "\nelse part in for loop:"

for i in range(10):
	print i, " ",
else:
	print "else part in for loop"
	
	
ls = [x for x in range(10)]
print ls

