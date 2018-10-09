# Uses python3
import sys
import decimal

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l
    return a*b

def gcd_pro(a,b):
    return recursive_mod(a,b)

def recursive_mod(a,b):
    # swap until a is bigger 
    if b > a:
        q = a
        a = b
        b = q

    m = a % b
    if m == 0:
        return b
    else:
        return recursive_mod(b,m)

def lcm_pro(a, b):
   # lcm =  (a*b)/GCD(a,b)
    return int(decimal.Decimal(a*b)/decimal.Decimal(gcd_pro(a,b)))

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_pro(a, b))

