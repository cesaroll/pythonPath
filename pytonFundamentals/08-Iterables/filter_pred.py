import math
from pprint import pprint as pp

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
    
def main():
    print("Is prime 2: {}".format(is_prime(2)))
    print("Is prime 3: {}".format(is_prime(3)))
    
    prime_numbers = [x for x in range(101) if is_prime(x)]
    print(prime_numbers)
    
    prime_square_divisors = {x*x:(1, x, x*x) for x in range (101) if is_prime(x)}
    pp(prime_square_divisors)
    
if __name__ == '__main__':
    main()