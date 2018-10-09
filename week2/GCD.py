# python3
def gcd_pro(a,b):
	# swap until a is bigger 
	if b > a:
		q = a
		a = b
		b = q
	
	return recursive_mod(a,b)

def recursive_mod(a,b):
	m = a % b
	if m == 0:
		return b
	else:
		return recursive_mod(b,m)

if __name__ == '__main__':
	input_numbers = [int(x) for x in input().split()]
	print(gcd_pro(input_numbers[0],input_numbers[1]))

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd
