# Uses python3
from sys import stdin

def fibonacci_sum_squares_pro(n):
    # so.. can't we just find the repeating pattern in the sum of last digit again?
    # does 99^2 have the same last digit as 9^2? probably. let's check!
    # yes, it does
    # so, since we know last digit of fib repeats at %60, we can use the same approach
    # simply figure out the sum of the last digit of squared fibs up to 60
    n %= period_of_sum_squares()
    return fibonacci_sum_squares_naive(n)
    pass

def period_of_sum_squares():
    a = 0
    b = 1
    s0 = 0
    s1 = 1
    for i in range(3,100):
        c = a + b
        a = b
        b = c
        s1 += pow(b,2)
        s1 %= 10
        if s0 == 0 and s1 == 1:
            return i-2
        s0 = s1
    

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_pro(n))
