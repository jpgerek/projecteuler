import math
import itertools
from euler import is_prime, gen_primes

ELEMENTS_NUM = 4
SEQUENCE_SIZE = 3
START_NUMBER = 10 ** (ELEMENTS_NUM-1)
MAX_NUMBER = (10**ELEMENTS_NUM)
MAX_INTERVAL = int(MAX_NUMBER/SEQUENCE_SIZE)

possible_primes = (prime for prime in gen_primes(limit=MAX_NUMBER) if prime >= START_NUMBER)

primes_seq = []
for sequence_first in possible_primes:
	for interval in xrange(2, MAX_INTERVAL, 2):
		sequence_second = sequence_first+interval
		if sequence_second > MAX_NUMBER or not is_prime(sequence_second):
			continue
		sequence_third = sequence_second+interval
		if sequence_third > MAX_NUMBER or not is_prime(sequence_third):
			continue
		list_1 = [d for d in str(sequence_first)]
		list_2 = [d for d in str(sequence_second)]
		list_3 = [d for d in str(sequence_third)]
		#- Sorting the digits list to compare them later, if the don't have the same order they aren't equal -#
		list_1.sort()
		list_2.sort()
		list_3.sort()
		#- Checking if the 3 primes with equal intervals are permutations of one another and have 4 elements -#
		if  list_1 == list_2 == list_3:
			primes_seq.append((sequence_first, sequence_second, sequence_third))
	else:
		#- It continues the outer loop if there wasn't a break in the inner loop -#
		continue
	#- It breaks if it didn't hit the else case of the inner loop -#
	break
for seq in primes_seq:
	print ''.join(map(lambda x: str(x), seq))