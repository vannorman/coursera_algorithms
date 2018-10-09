from fibonacci_sum_last_digit import *
def test():
    a = int(input("How many tests? "))
    b = int(input("Starting number? "))
    for i in range(a):
        naive = fibonacci_sum_naive(i + b)
        pro = fib_sum_pro(i+b)
        if naive == pro:
            result = "PASS"
        else:
            result = "FAIL"
        print("i:"+str(i+b)+", naive;"+str(naive)+", pro:"+str(pro)+"; result;"+result)
        if result == "FAIL":
            print("failed after "+str(i)+" tries.")
            return     
