from euler import cf_fraction
from math import log10, floor

LIMIT = 1000

cf_digits = [1]
sqrt_2_period_digit = 2
fractions = []
for n in xrange(1, LIMIT):
	cf_digits.append(sqrt_2_period_digit)
	numerator, denominator = cf_fraction(cf_digits)
	if floor(log10(numerator)) > floor(log10(denominator)):
		fractions.append((numerator, denominator))
print len(fractions)