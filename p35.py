import math
import itertools
from euler import is_prime, gen_primes

def is_circular_prime(prime):
	digits = [c for c in str(prime)]
	for x in xrange(0,len(digits)):
		digits.append(digits.pop(0))
		rotated_num = int(''.join(digits)) 
		if not is_prime(rotated_num):
			return False
	return True

print len([prime for prime in gen_primes(1000000) if is_circular_prime(prime)])
