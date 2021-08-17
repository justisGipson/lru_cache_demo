from functools import lru_cache

computing_times = 0

@lru_cache(maxsize=None)
def fib(n):
	global computing_times
	computing_times += 1

	if n < 2:
		return n
	print(computing_times)
	return fib(n-1) + fib(n-2)

for n in range(10):
	_ = fib(n)


'''
output:
3
4
5
6
7
8
9
10
'''
