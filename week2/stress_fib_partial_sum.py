from fibonacci_partial_sum import *
import random
def test():
    a = int(input("How many tests? "))
    b = int(input("Start from what number? "))
    c = int(input("Avg spread? "))
    for i in range(a):
        from_ = i + b
        to = from_ + max(1,int((random.random() + 0.5) * c))
        naive = fibonacci_partial_sum_naive(from_,to)
        pro = fib_partial_sum_pro(from_,to)
        print("Testing range "+str(from_)+" to "+str(to)+" ... ",end='')
        if naive == pro:
            print("PASS: "+str(i+b)+", naive:"+str(naive)+", pro:"+str(pro))
        else:
            print ("FAIL! naive;"+str(naive)+", pro:"+str(pro)+" at i;"+str(i+b))
            return
