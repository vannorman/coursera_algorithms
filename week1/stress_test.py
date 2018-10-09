import max_pairwise_product
import random

def run():
    arr = [4,5,6,7,8,1,2,3,4,5,]

    N = input('How many test cases? : ')
    n = input('Average count of integers per test case? : ')
    s = input('Average integer value? : ')
    try:
        N = int(N)
        n = int(n)
        s = int(s)
    except:
        print("One of the values you entered could not be parsed into an integer.")
        print("Exiting")
        return
        

    print("Generating "+str(N)+" arrays of average length "+str(n),end='')
    for i in range(N):
        print(" test case "+str(i)+": Efficient: ",end='')
        count = random.randint(int(n/10),n*2)
        arr = []
        for j in range(count+2): # add 2 for minimum array size of 2
            num = random.randint(int(s/10),s*2) 
            arr.append(num)
        result_efficient = max_pairwise_product.max_pairwise_product(arr)
        result_naive = max_pairwise_product.max_pairwise_product_naive(arr)
        print(str(result_efficient),end='')
        print(", Naive:"+str(result_naive),end='')
        result = "FAIL"
        if result_efficient == result_naive:
            result = "PASS" 
        print(", RESULT? : "+result)
        if result == "FAIL": 
            print("exiting ..")
            return;
        
        

run() 



