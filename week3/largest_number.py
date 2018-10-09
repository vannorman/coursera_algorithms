#Uses python3

import sys

def largest_number(a):
    #write your code here
    res = ""
    s = sorted(a, key = lambda x: int(str(x)[0]), reverse = True) 
    for x in s:
        res += x
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
