from euler import is_prime, is_truncatable_prime
import itertools

NUM_OF_PRIMES = 11
VALID_DIGITS = (1, 2, 3, 5, 7, 9)
truncatable_primes = []

for repeat in itertools.count(start=2): 
	for candidate_product in itertools.product(VALID_DIGITS, repeat=repeat):
		if is_truncatable_prime(candidate_product):
			truncatable_primes.append(int(''.join(map(str, candidate_product))))
			if len(truncatable_primes) == NUM_OF_PRIMES:
				break
	#- Makes the inner loop exiting the outer one when doing 'break' -#
	else:
		continue
	break

print sum(truncatable_primes)