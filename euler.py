import itertools
import math


def fibonacci(limit=0):
	prev = 1
	current = 0
	aux = 0
	while True:
		aux = current
		current = prev + current
		prev = aux
		if limit == 0 or current < limit:
			yield current
		else:
			return

def is_prime(num, cached_primes=set()):
	if num in cached_primes:
			return True
	if num == 1:
			return False
	if num == 2:
			return True
	if num % 2 == 0:
			return False
	for multiple in xrange(3, int(math.sqrt(num)) + 1, 2):
			if num % multiple == 0:
					return False
	cached_primes.add(num)
	return True

def get_factors(num):
	factors = set([1, num])
	limit = int(math.sqrt(num))
	for multiple in xrange(2, limit+1): 
		if num%multiple == 0:
			factors.add(multiple)
			factors.add(num/multiple)
	return factors

def gen_primes(limit=0):
	yield 2
	yield 3
	for k in itertools.count(start=1):
		num_minus = 6 * k - 1
		num_plus = num_minus + 2
		if num_minus > limit:
			return
		if is_prime(num_minus):
			yield num_minus
		if num_plus > limit:
			return
		if is_prime(num_plus):
			yield num_plus

def is_pandigital(num, digits=9):
	num_str = str(num)
	if num_str.find('0') != -1:
		return False
	ordered_try = set(int(d) for d in num_str)
	return len(ordered_try) == digits

def is_truncatable_prime(digits):
	digits_length = len(digits)
	#- Removing from the right and the left and checking if they are prime -#
	for slice_order in (lambda offset: digits[-offset:], lambda offset: digits[:-offset]):
		for offset in xrange(1, digits_length):
			num = int(''.join(map(str, slice_order(offset))))
			if not is_prime(num):
				return False
	whole_num = int(''.join(map(str, digits)))
	if not is_prime(whole_num):
		return False
	return True