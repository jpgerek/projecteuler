from itertools import islice
from euler import cf_number_e, cf_fraction

LIMIT = 100
cf_digits = list(islice(cf_number_e(), LIMIT))
numerator, denominator = cf_fraction(cf_digits)
print sum(map(lambda str_digit: int(str_digit), (str_digit for str_digit in str(numerator))))