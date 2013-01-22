import math
import itertools
from euler import gen_primes, is_prime

A_LIMIT = 1000
B_LIMIT = 1000

product = (0, 0)
max_n = 0
for a in xrange(-A_LIMIT+1, A_LIMIT):
	#- b has to be a primer number always -#
	for b in gen_primes(B_LIMIT):
		for n in itertools.count():
			#- Absolute value of the quadratic formula result -#
			num = abs((n**2) + (a*n) + b)
			if not is_prime(num):
				break
		if n > max_n:
			max_n = n
			product = (a, b)
a, b = product
print "n = %d, a = %d, b = %d, a*b = %d" % (max_n, a, b, a*b)
