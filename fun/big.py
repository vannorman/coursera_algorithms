
def big():
    a = input("How big? a:")
    b = input("How big? b:")
    c = input("How big? c:")
    for i in range(a):
        for j in range(b):
            for k in range(c):
                for l in range(a):
                    a *= (b*c)
                    print("a:"+str(len(str(a))))

big()
