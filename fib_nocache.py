computing_times = 0

def fib(n):
	global computing_times
	computing_times += 1
	
	if n < 2:
		return n
	print(computing_times)
	return fib(n-1) + fib(n-2)


for n in range(10):
	fib(n)
