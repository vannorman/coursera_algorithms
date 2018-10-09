#e Uses python3
import sys
# from fibonacci_pro import * #wont work for submissions

def calc_fib_pro(n):
    a = 0
    b = 1
    if n == 0: return 0
    for i in range(n-1):
        c = b
        b = a + b
        a = c
    return b



def get_fib_last_digit_pro(n):
    # idea: the sequence of last digits is regular
    interval = fib_repitition_period()
    n %= interval
    if n == 0: return 0
    a = 0
    b = 1
    
    for i in range(n-2):
        c = b
        b = (a + b) % 10 # keep only the ones digit
        a = c
    return b


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10

def fib_repitition_period():
    # max n ensures we only do a search of, say, 100 numbers (I happen to know the period will happen at N=60)
    max_n = 100
    # the first repition will be of F[0] and F[1]

    for i in range(0,max_n):
        f = calc_fib_pro(i) % 10 # 1's digit of the i-th fib number
#       print(str(i)+": "+str(f))
        if i > 2 and f == 1 and f0 == 1:
#           print (colored.fg('red') + "matched 1,1 at index "+str(i) + colored.attr('reset'))
            return i - 1 # the i-th check is inclusive of the 2 digits at the front and the matching 2 digits at the back, so subtract 2 to get the period, then add one because we started counting at 0
        f0 = f


 
if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fib_last_digit_pro(n))



   

