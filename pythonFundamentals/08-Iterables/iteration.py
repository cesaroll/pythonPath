import math
from itertools import islice, count

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def sumPrimes(maxNu
    return sum(islice((x for x in count() if is_prime(x)), maxNum) )

def run_sumPrimes():
    print(sumPrimes(1000))

if __name__ == '__main__':
    run_sumPrimes()