# Uses python3
import sys

def get_change(m):
    m_ = m
    coins = []
    coin_types = [10,5,1]
    for c in range(len(coin_types)):
        for n in range(int(m/coin_types[c])):
            coins.append(coin_types[c]) 
            m -= coin_types[c]
            print("add:"+str(c)+", m;"+str(m))
    print("using coins:"+str(coins)+" to make "+str(m_))
    return len(coins)

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
