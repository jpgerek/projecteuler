from euler import is_pandigital

DIGITS = 9
products = []
RANGE_LIMIT = 10**(DIGITS/3+1)
b_cache  = {}
for a in xrange(1, RANGE_LIMIT):
	for b in xrange(1, int(RANGE_LIMIT/a)):
		result = a * b
		number_str = str(a) + str(b) + str(result)
		if len(number_str) > DIGITS:
			continue
		if number_str.find('0') != -1:
			continue
		if is_pandigital(number_str):
			if a in b_cache:
				break
			b_cache[b] = True
			# print a, b, result
			products.append(result)
	else:
		continue
	break
print sum(set(products))