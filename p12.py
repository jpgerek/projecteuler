import itertools
import math
from euler import factors


def gen_triangle_nums():
	num = 0
	count = 1
	while True:
		num = num + count
		yield num
		count += 1

for num in gen_triangle_nums():
	factors_digits = factors(num)
	if len(factors_digits) > 500:
		print num
		break