# Uses python3
def calc_fib_naive(n):
    if (n <= 1):
        return n
    return calc_fib_naive(n - 1) + calc_fib_naive(n - 2)

def calc_fib_pro(n):
    a = 0
    b = 1
    print ("hi")
    if n == 0: return 0
    for i in range(n-1):
        c = b
        b = a + b
        a = c
    return b

n = int(input())
print(calc_fib_pro(n))

def calc_fib(n):
    a = calc_fib_pro(n)
    b = calc_fib_naive(n)
#   print("testing nth fibonacci number:"+str(n),end='')
    print(" ... results .... PRO: "+str(a),end="")
    print(", NAIVE: "+str(b),end='')
    if a == b: result = "PASS"
    else: result = "FAIL"
    print(", pass? "+result)


