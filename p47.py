import math
import itertools
from euler import is_prime, gen_primes

def prime_factors(num):
	factors_set = set()
	limit = int(math.sqrt(num))+1
	for multiple in xrange(2,limit+1):
		if num%multiple == 0:
			other_multiple = num/multiple
			if is_prime(multiple):
				factors_set.add(multiple)
			if is_prime(other_multiple):
				factors_set.add(other_multiple)
	return factors_set

limit = 4
con_nums = []
for num in itertools.count(1):
	factors = prime_factors(num)
	if len(factors) == limit:
		con_nums.append(num)
		if len(con_nums) == limit:
			break;	
	else:
		con_nums = []
print con_nums[0]
