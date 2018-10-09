# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n
    previous = 0
    current  = 1
    for _ in range(n - 1):
        previous, current = current, previous + current
    return current % m

def get_fib_huge_pro(n, m):
    interval = fib_repitition_period(m)
    n %= interval
    return calc_fib_pro(n) % m 

def get_fib_huge_naive_2(n, m):
    pattern = []  
    for i in range(m * m):#? Unsure what's a lower bound for safely finding the repeating pattern 
        # we don't want to check after every i
        # what is the optimal checking pattern for the pisano period?
        # let's assume it's safe to calc every m values

        # all the gibberish below is not needed, we don't need to compare the whole list, we only need to match the first two values, because once two values match the pattern is guaranteed to repeat 
        pattern.append(calc_fib_pro(i) % m) # add current number to the list
        if i % m == 0 or i >= m * m - 1:
            # [ 5, 6, 7, 1, 2, 3, 4, 1, 1, 5, 6, 7, 1, 2, 3, 4, 1, 1, 5, 6 ] 
            cont = True
            for j in range(3,int(len(pattern)/2)):
                print("\n")
                # iterate through each number in the pattern. For each number, try to match it with the start of the list.
                # if pattern[j] thru pattern[2j] matches from start of list pattern[0] through pattern[j-1], success!
                result = "PASS"
                k_arr_len = min(len(pattern)-j,j)
                for k in range(k_arr_len):
                    if pattern[j+k] is not pattern[k]:
                        result = "FAIL"
                        print("FAIL.."+str(j+k)+": "+str(pattern[j+k])+", "+str(k)+":"+str(pattern[k]))
                        break
                    else:
                        print(str(j+k)+": "+str(pattern[j+k])+", "+str(k)+":"+str(pattern[k]))
                if result == "PASS":
                    print("Passed! ;"+result)
                    return k_arr_len
            print("pattern:  "+str(pattern))
    

def get_fib_last_digit_pro(n):
    # idea: the sequence of last digits is regular
#   interval = fib_repitition_period()
#   n %= interval
#   if n == 0: 
#       return 0

    interval = fib_repitition_period()
    n %= interval
    return calc_fib_pro(n) % 10

#    if n == 0: return 0
#    a = 0
#    b = 1
#    for i in range(n-2):
#        c = b
#        b = (a + b) % 10 # keep only the ones digit
#        a = c
#    return b

def calc_fib_pro(n):
    a = 0
    b = 1
    if n == 0: return 0
    for i in range(n-1):
        c = b
        b = a + b
        a = c
    return b

def fib_repitition_period(m=10): # last digit repitition
    for i in range(0,m*m):
        f = calc_fib_pro(i) % m # 1's digit of the i-th fib number
        if i > 2 and f == 0 and f0 == 1:
            return i
        f0 = f


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fib_huge_pro(n, m))


