# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    s = sorted(zip(weights,values), key = lambda x: x[1]/x[0], reverse = True)
    val = 0
    for item in s:
        if item[0] <= capacity:
            print("item :"+str(s))
            capacity -= item[0]
            val += item[1]
        else:
            print("item fill:"+str(s))
            capacity = 0 # full
            val += item[1] * capacity / item[0]  
            break
    return val


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
