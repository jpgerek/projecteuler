from euler import relative_primes

LIMIT = 10 ** 6

def phi(n):
	return len(list(relative_primes(n)))

#- After studying the numbers with the largest ratios n/phi(n) I realized they were multiples of 2310 -#
multiple = 2310
print max((float(n) / phi_n, n) for n, phi_n in ((n, phi(n)) for n in xrange(multiple, LIMIT+1, multiple)))