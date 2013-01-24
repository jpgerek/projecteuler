import itertools

special_pandigitals = []

for permutation in itertools.permutations('0123456789'):
	d1, d2, d3, d4, d5, d6, d7, d8, d9, d10 = permutation
	if int(''.join([d2, d3, d4])) % 2 == 0 and \
	   int(''.join([d3, d4, d5])) % 3 == 0 and \
	   int(''.join([d4, d5, d6])) % 5 == 0 and \
	   int(''.join([d5, d6, d7])) % 7 == 0 and \
	   int(''.join([d6, d7, d8])) % 11 == 0 and \
	   int(''.join([d7, d8, d9])) % 13 == 0 and \
	   int(''.join([d8, d9, d10])) % 17 == 0:
			special_pandigitals.append(int(''.join(permutation)))

print sum(special_pandigitals)