from itertools import ifilter
LIMIT = 10**7

LAST_LINK_GOOD = 89
LAST_LINK_BAD = 1

def square_digits_chain(number, cache={}, cache_limit=500):
	chain = [number]
	tmp_number = number
	while True:
		tmp_number = sum(map(lambda str_digit: int(str_digit)**2, (str_digit for str_digit in str(tmp_number))))
		chain.append(tmp_number)
		if tmp_number in cache:
			chain += cache[tmp_number]
			break
		if tmp_number in (LAST_LINK_BAD, LAST_LINK_GOOD):
			break
	#- Avoiding duplicate when is the last good link or the last good link -#
	if chain[-2] in (LAST_LINK_BAD, LAST_LINK_GOOD):
		chain.pop()
	if number not in cache and number < cache_limit:
		cache[number] = chain
	return chain

print sum((1 for x in ifilter(lambda chain: chain[-1] == LAST_LINK_GOOD, (square_digits_chain(number) for number in xrange(1, LIMIT)))))