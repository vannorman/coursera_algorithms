from fibonacci_sum_squares import *
def test():
    a = int(input("How many tests? "))
    b = int(input("Start from? "))
    for i in range(b,b+a):
        pro = fibonacci_sum_squares_pro(i) 
        naive = fibonacci_sum_squares_naive(i) 
        if pro == naive:
            print(str(i)+": Pass ("+str(pro)+")")
        else:
            print("Fail at "+str(i)+". pro:"+str(pro)+", naive:"+str(naive))
            return -1


