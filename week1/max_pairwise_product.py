# python3
def max_pairwise_product(numbers):
    a = 0
    b = 1
    for i in range(len(numbers)): 
        if (numbers[i] > numbers[a]): 
            b = a
            a = i # save the index, not the number, as two max nums may be the same
  
        elif (numbers[i] > numbers[b] and i != a): 
            b = i 
#    print("about to return a:"+str(a)+", b:"+str(b)+" on array;"+str(numbers),end='')
    return numbers[a] * numbers[b] 

def max_pairwise_product_naive(numbers):
    sorted_numbers = sorted(numbers)
    size = len(numbers)
    return sorted_numbers[size-1] * sorted_numbers[size-2] 
  
if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))

