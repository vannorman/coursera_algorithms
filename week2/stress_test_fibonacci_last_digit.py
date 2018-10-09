from fibonacci_last_digit import *
import random
from fibonacci_last_digit import *

def test():
	a = int(input("How many fibs? "))
	c = "YN"
	while c != "Y" and c != "N":
		if c != "YN":
			print("Invalid: "+c)
		c = input("Do sequential? (Y/N) ")
	if (c == "Y"):
		b = int(input("start at which fib? "))
		for i in range(a):
			print (str(i)+" : ",end='')
			naive = get_fibonacci_last_digit_naive(b+i)
			pro = get_fib_last_digit_pro(b+i)
			check(pro,naive)
	else:
		b = int(input("Average size of fib? "))
		for i in range(a):
			print (str(i)+" : ",end='')
			f = int(random.random()*b*2)
			naive = get_fibonacci_last_digit_naive(f)
			pro = get_fib_last_digit_pro(f)
			check(pro,naive)

def check(pro,naive):
	print("NAIVE result:"+str(naive),end='')
	print(".. PRO result:"+str(pro),end='')
	if naive == pro:
		result = "PASS"
	else:
		result = "FAIL" 
	print('.. result:'+result)
		
