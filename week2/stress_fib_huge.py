from fibonacci_huge import *
def test():
    a = int(input("how many tests? "))
    b = int(input("starting no? "))
    c = int(input("mod what? "))
    for i in range(b,a+b):
        naive = get_fibonacci_huge_naive(i,c)
        pro = get_fib_huge_pro(i,c)
        if naive == pro:
            print(str(i)+": PASS ( "+str(pro)+")");
        else:
            print("FAIL AT "+str(i)+", naive;"+str(naive)+", pro;"+str(pro))
            return -1
        

