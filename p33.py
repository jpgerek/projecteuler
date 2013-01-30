from itertools import product
from euler import gcd

result = []

for d1, d2 in product(xrange(1, 10), xrange(1, 10)):
	denominator = d1 * 10 + d2
	for n1, n2 in product(xrange(1, d1+1), xrange(1, 10)):
		numerator = n1 * 10 + n2
		if numerator >= denominator:
			break
		fraction_result = float(numerator) / float(denominator)
		numerator_digits = [n1, n2]
		denominator_digits = [d1, d2]
		common_digits_iter = (digit for digit in numerator_digits if digit in denominator_digits)
		for common_d in common_digits_iter:
			numerator_digits.remove(common_d)
			denominator_digits.remove(common_d)
			tmp_num = numerator_digits[0]
			tmp_den = denominator_digits[0]
			if float(tmp_num) / float(tmp_den) == fraction_result:
				result.append((tmp_num, tmp_den))
			break
		
numerator, denominator = reduce(lambda (n1, d1), (n2, d2): (n1 * n2, d1 * d2), result)
print denominator / gcd(numerator, denominator)