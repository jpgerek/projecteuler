import math
import itertools

def is_prime(num, do_cache=False, cached_primes=set()):
        if do_cache and num in cached_primes:
                return True
        if num == 1:
                return False
        if num == 2:
                return True
        if num%2 == 0:
                return False
        for multiple in xrange(3, int(math.sqrt(num))+1, 2):
                if num % multiple == 0:
                        return False
	if do_cache:
		cached_primes.add(num)
        return True

def gen_primes(limit=0):
	yield 2
	yield 3
	for k in itertools.count(1):
		num_minus = 6*k-1
		num_plus = num_minus+2
		if num_minus > limit:
			return
		if is_prime(num_minus):
			yield num_minus
		if num_plus > limit:
			return
		if is_prime(num_plus):
			yield num_plus


def can_be(num):
	for prime in gen_primes(num):
		base = int(math.sqrt((num-prime)/2))
		if num == (prime + 2*base*base):
			#print "%d = %d + 2x%dx%d" % (num, prime, base, base)
			return True
	return False


for num in itertools.count(9,2):
	if not can_be(num):
		print num
		break	
