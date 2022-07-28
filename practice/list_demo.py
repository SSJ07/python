## list demo

if __name__=='__main__':
	ls = range(10)
	print "list is :",ls
	print "length of list :", len(ls)
	ls.reverse()
	print "reverse list is:", ls
	ls.sort()
	print "sort list :", ls
	ls.append(100)
	print "append value to list :", ls
	print "count any value in list:", ls.count(1)
	print "pop item in list", ls.pop()
	ls.remove(2)
	print "remvoe item in list", ls
	ls.extend([20,30,40,50])
	print "extend list by another list ", ls
	
