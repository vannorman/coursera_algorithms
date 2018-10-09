# Uses python3
import sys

def fib_sum_repitition_period(m=10):
    a = 0
    b = 1
    s0 = 0
    s1 = a + b
    for i in range(2,m*m):
        c = a + b
        a = b
        b = c % 10
        if i > 3 and s0 == 0 and s1 == 1:
#            print("sums are 01")
            return i - 2
        s0 = s1
        s1 += b
        s1 %= 10
#        print("i:"+str(i)+", b:"+str(b)+", s0:"+str(s0)+", s1:"+str(s1))



def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

def fib_sum_n(n):
    a = 0
    b = 1
    s = 1
    if n == 0: return 0
    for i in range(n-1):
        c = a + b
        a = b
        b = c % 10
        s += b
        s %= 10
#        print("i;"+str(i)+", b:"+str(b)+", s:"+str(s))
    return s # is zero for n=60 so the sum of N % 60 fib numbers is 0..




def fib_sum_pro(n):
    # well, since the period of the last digit value repeats (at 60), 
    # we can simply take the sum of the first 60, %60 to the number we got, and sum those
    # or, we can find the period of repitition for the sum of fib numbers (faster)
    n %= fib_sum_repitition_period()
    return fib_sum_n(n)

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fib_sum_pro(n))


