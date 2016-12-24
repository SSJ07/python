'''
	This program counts each character frequency in given string.
'''

def count_char_freq(string):
	ds = {}
	for i in string:
		if ds.has_key(i):
			ds.update({i:ds.get(i)+1})
		else:
			ds[i]=1
	return ds


if __name__=='__main__':

	#take input from keyboard
	string = raw_input("Enter any string :")
	char_freq = count_char_freq(string)
	print "Char freq is :"
	for key, value in char_freq.iteritems():
		print "%s : %s"%(key, value)

