from GCD import * 
from random import random
def test():
    n = int(input("how many tests? ") )
    a = int(input("Starting num size (a)? "))
    b = int(input("Starting num size (b)? "))
    for i in range(n):
        n1 = i + int(a * random() * 2)
        n2 = i + int(b * random() * 2)
        naive = gcd_naive(n1,n2)
        pro = gcd_pro(n1,n2) 
        if pro == naive:
            result = "PASS"
        else:
            result = "FAIL"
        print(str(i)+" ( "+str(n1) + ","+ str(n2) + ") : NAIVE:"+str(naive)+", PRO:"+str(pro)+", result;"+result)
        if result == "FAIL":
            return "Test failed after "+str(i)+" tries"
         

