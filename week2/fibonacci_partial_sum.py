# Uses python3
import sys

def fib_partial_sum_pro(from_, to):
    # we can simply use the same as sum_last_digit_pro but subtract the first from the second.
    # if it goes negative, take %10
    # make sure to subtract 1 from from, as it's inclusive 
#    print("from: "+str(from_)+" to " + str(to))
   # , %60:"+str(from_%60)+", fib sum n:"+str(fib_sum_n(from_%60)))
#    print("sum of digits 0 to from - 1:"+str(fib_sum_n(from_%60-1)))
#    print("sum of digits 0 to to:"+str(fib_sum_n(to%60)))
    a = fib_sum_n(to%60)
    b = fib_sum_n((from_-1)%60)
 #   print("diff;"+str(a)+" - "+str(b)+" = "+str(a-b))

  #  print("fib sum  % 60:"+str(a)+", fib sum from % 60:"+str(b)+", dif:"+str((a-b)%10))
    return (a-b)%10

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

 

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
#    print(fibonacci_partial_sum_naive(from_, to))
    print(fib_partial_sum_pro(from_,to))
