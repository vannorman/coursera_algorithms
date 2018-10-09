def run():
    print("This will return the value of an up arrow notation of the form a↑..↑c with n ↑s.")
    a = int(input("Enter first term (a):"))
    n = int(input("How many up arrows (n):"))
    b = int(input("Enter second term (b):"))
    n_string = ""
    for i in range(n):
        n_string += "↑"
    print("Ok, calculating "+str(a)+n_string+str(b))
    print(up_arrow(a,n,b))

def up_arrow(a,n,b):
    if n == 0:
        return a * b
    elif n >= 1 and b ==0:
        return 1
    else:
        return up_arrow(a,n-1, up_arrow(a,n,b-1))

def up_arrow_2(a,b,c):
    # I want to repeat up_arrow(b-1) b times
    if b == 1:
        for i in range(c):
            a *= a
        return a
    for i in range(b):
        a *= up_arrow(a,b-1,c)
    print(str(a))
    return a

    if b == 1:
        for i in range(c):
            print("a *= a where a == "+str(a))
            a *= a
        print("result:"+str(a))
        return a
    else:
        d = a
        for i in range(c):
            print("iterated uparrow where a:"+str(a)+", b:"+str(b)+", c:"+str(c))
            d *= up_arrow(a,b-1,c)
        return d
    
    

run()

