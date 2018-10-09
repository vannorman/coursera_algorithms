from termcolor import colored

import fibonacci
def run_clever():
    n = int(input("How many fibs?"))
    for i in range(1,n): # skip zeroth term, an artifact of picking 1, 1 as starting sequence
        f = fibonacci.calc_fib_pro(i) % 10 # 1's digit of the i-th fib number
        if i > 2 and f == 1 and f0 == 1:
            print (colored("matched 1,1 at index "+str(i),'red'))
        f0 = f
#

def run_naive():
    f0 = -1
    n = input("How many?")
    n = int(n)
    vals = []
    prev_match_index = 0
    for i in range(1,n):
        
        f = fibonacci.calc_fib_pro(i) % 10
        print(str(i)+": "+str(f)) 
        for j in range(prev_match_index,len(vals)):
            if j > 0:
               if vals[j-1] == f0 and vals[j] == f and prev_match_index == 0:
                    print (colored("matched at "+str(j),'red'))
                    prev_match_index = j
                    break
        f0 = f
        vals.append(f)


run_clever()
