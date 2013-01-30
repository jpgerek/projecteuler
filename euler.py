import itertools
import math
import matplotlib.pyplot as plot
import sys

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

def factors(num, cache={}):
	if num in cache:
		return cache[num]
	factors = set([1, num])
	limit = int(math.sqrt(num))
	for candidate in xrange(2, limit+1): 
		if num % candidate == 0:
			factors.add(candidate)
			factors.add(num / candidate)
	cache[num] = factors
	return factors

def relative_primes(num):
	num_factors = factors(num)
	candidates = set(xrange(1, num))
	set_1 = set((1, ))
	yield 1
	for candidate in candidates.difference(num_factors):
		if factors(candidate).intersection(num_factors) == set_1:
			yield candidate
	
def relative_primes(num):
	yield 1
	num_factors = factors(num)
	num_factors.remove(num)
	set_1 = set((1, ))
	#- If it has just 1 as factor it's prime-#
	if num_factors == set_1:
		return
	candidates = set(xrange(1, num))
	for candidate in candidates.difference(num_factors):
		if factors(candidate).intersection(num_factors) == set_1:
			yield candidate

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

def is_palindromic(num):
	str_num = str(num)
	return str_num == str_num[::-1]

def show_chart(xs, ys, xlabel = 'n', ylabel='Seconds', title=False):
	#- By default setting as title caller's file name -#
	title = title if title else sys._current_frames().values()[0].f_back.f_globals['__file__'] 
	ax = plot.subplot(111)
	ax.plot(xs, ys)
	ax.set_ylabel(ylabel)
	ax.set_xlabel(xlabel)
	ax.set_title(title)
	plot.show()
	
def quadratic(a, b, c):
	if a == 0:
		raise ValueError("a can't be zero.")
	tmp = (b * b) - (4 * a * c)
	if tmp < 0:
		raise ValueError("There aren't real solutions for: %s, %s, %s." % (a, b, c))
	sqrt_part = math.sqrt(tmp)
	denominator = 2 * a
	return [(-b + (sign * sqrt_part)) / denominator for sign in (-1, 1)]

#- Borrowed from http://eli.thegreenplace.net/2009/06/19/project-euler-problem-66-and-continued-fractions/ -#
def cf_sqrt(n):
    """ Compute the continued fraction representation of the
        square root of N.

        The first element in the returned array is the whole
        part of the fraction. The others are the denominators
        up to (and not including) the point where it starts
        repeating.

        Uses the algorithm explained here:
        http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/cfINTRO.html#sqrtalgs
    """
    n_sqrt = math.sqrt(n)
    n_sqrt_floor = math.floor(n_sqrt)
    #- The root is an integer -#
    if n_sqrt_floor == n_sqrt:
        return [n_sqrt_floor]

    ans = []

    step1_num = 0
    step1_denom = 1

    while True:
        nextn = int((n_sqrt_floor + step1_num) / step1_denom)
        ans.append(nextn)

        step2_num = step1_denom
        step2_denom = step1_num - step1_denom * nextn

        step3_denom = (n - step2_denom ** 2) / step2_num
        step3_num = -step2_denom

        if step3_denom == 1:
			ans.append(ans[0] * 2)
			break

        step1_num, step1_denom = step3_num, step3_denom

    return ans

def cf_number_e():
 	yield 2
 	for k in itertools.count(start=1):
 		yield 1
 		yield 2*k
 		yield 1
 		
def cf_fraction(cf_digits):
	"""
	Converts a sequence of digits from a continued fraction into a tuple
	of the form numerator and denominator.
	"""
	numerator = 1
	denominator = cf_digits[-1]
	for digit in itertools.islice(reversed(cf_digits), 1, len(cf_digits)):
		numerator = (digit * denominator) + numerator
		numerator, denominator = denominator, numerator 
	return denominator, numerator

def pentagonal(n):
	return n * ((3 * n) - 1) / 2
	
def is_pentagonal(number):
	n = float(math.sqrt(24 * number + 1) + 1) / 6.0
	return n == int(n)