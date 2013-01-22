import itertools
from euler import is_prime

max_prime_pandigital = 0
for n in reversed(xrange(2,10)):
	for pandigital_set in reversed(list(pandigital_set for pandigital_set in itertools.permutations(range(1,n)))):
		pandigital = int(''.join(map(lambda x: str(x), pandigital_set)))
		if is_prime(pandigital):
			max_prime_pandigital = pandigital
			break
	else:
		continue
	break
print max_prime_pandigital