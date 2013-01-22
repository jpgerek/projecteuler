import math
from euler import is_prime

def prime_factors(num):
	factors_set = set()
	for multiple in xrange(3, int(math.sqrt(num))+1, 2):
		if num%multiple == 0:
			other_multiple = num/multiple
			if is_prime(multiple):
				factors_set.add(multiple)
			elif is_prime(other_multiple):
				factors_set.add(other_multiple)
	return factors_set

print max(prime_factors(600851475143))
