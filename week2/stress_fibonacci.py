import fibonacci
import random

def run():
    N = int(input('How many test cases? : '))
    for i in range(N):
        print("i:"+str(i)+" .. "+str(fibonacci.calc_fib_pro(i) % 10))

def run_rand():
    N = int(input('How many test cases? : '))
    f = int(input('Average fibonacci index? : '))
    for i in range(N):
        num = random.randint(int(f/10),f*2)
        fibonacci.calc_fib(num)

run()
        
         
    

