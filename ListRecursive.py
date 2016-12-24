ls = [5,1,[3,2,[10,9,[6],8],1],4,3,[8,5,3,1,[12,60,6,10],0]]
print "Before sorting :", ls

def mySort(val):
	for i in val:
		if isinstance(i, list):
			index = val.index(i)
			i.sort()
			val[index]=i
			mySort(i)
		
			

ls.sort()
mySort(ls)
print "After Sorted List is :" , ls
l = []
def combineList(val):
	for i in val:
		if isinstance(i, list):
			combineList(i)
		else:
			l.append(i)

combineList(ls)
l.sort()
print "After Combining List:", l

