from euler import is_pandigital

DIGITS = 9
max_pandigital = ''
RANGE_LIMIT = 10**(DIGITS/3+1)
quit_flag = False
for a in reversed(xrange(1, RANGE_LIMIT)):
	for b in xrange(1, RANGE_LIMIT):
		result = a * b
		max_pandigital += str(result)
		if len(max_pandigital) > DIGITS:
			max_pandigital = ''
			break
		if max_pandigital.find('0') != -1:
			max_pandigital = ''
			break
		if is_pandigital(max_pandigital):
			quit_flag = True
			break
	if quit_flag:
		break
print max_pandigital
