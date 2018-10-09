def calc_fib_pro(n):
	a = 1
	b = 1
	for i in range(n-1):
		c = b
		b = a + b
		a = c
	return b


