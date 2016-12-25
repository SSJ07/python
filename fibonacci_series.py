#fibonacci series

def fib(n):
	if n==0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)


if __name__=='__main__':
	num = input("Enter number :")
	fib_num = fib(num)
	print "fib_num is :" + str(fib_num)
	
