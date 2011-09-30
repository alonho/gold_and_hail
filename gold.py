from itertools import ifilter
from warnings import warn

RANGE = 2**20

try:
    import numpy
except ImportError:
    warn("install numpy for better performance")
    
    def isprime(n):
        # 0 and 1 are not primes
        if n < 2:
            return False
        # 2 is the only even prime number
        elif n == 2: 
            return True    
        # all other even numbers are not primes
        if not n & 1: 
            return False
        # range starts with 3 and only needs to go up the squareroot of n
        # for all odd numbers
        for x in range(3, int(n**0.5)+1, 2):
            if n % x == 0:
                return False
        return True

    def get_primes(max_num):
        return ifilter(isprime, xrange(max_num))

else: # numpy is supported!
    def get_primes(limit):
        is_prime = numpy.ones(limit + 1, dtype=numpy.bool)
        for n in xrange(2, int(limit**0.5 + 1.5)): 
            if is_prime[n]:
                is_prime[n*n::n] = 0
        return numpy.nonzero(is_prime)[0][2:]

primes = set(get_primes(RANGE))

def get_parts(n):
    for prime in primes:
        candidate = n - prime
        # set has O(1) complexity for average case
        if candidate in primes:
            return (prime, candidate)
    assert False, n

def main_iter():
    for i in xrange(4, RANGE, 2):
        yield i, get_parts(i)

def main_verbose():
    for (n, (a, b)) in main_iter():
        print "{} = {} + {}".format(n, a, b)

def main_silent():
    for _ in main_iter(): pass

if __name__ == '__main__':
    main_silent()

