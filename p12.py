import itertools
import math
from euler import get_factors


def gen_triangle_nums():
	num = 0
	count = 1
	while True:
		num = num + count
		yield num
		count += 1

for num in gen_triangle_nums():
	factors = get_factors(num)
	if len(factors) > 500:
		print num
		break