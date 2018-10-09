# Uses python3
import sys

# 14
# 1 2 3 4 !4
def optimal_summands(n):
    summands = []
    for i in range(1,n):
        # if the remainder after n - i would be *less* than the current number, simply use the remainder as the final
        # 8: -1 = 7: -2 = 5: -3 doesn't work because 5 - 3 < current index of 2 
        if n - i - (i + 1) < i:
            summands.append(n)
            break
        else:
            summands.append(i)
            n -= i
            
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
