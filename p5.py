import math
import itertools
from euler import is_prime

def is_divisible(divisible_num, limit):
	for num in xrange(2, limit+1):
		if divisible_num%num != 0:
			return False
	return True

limit = 20
step = reduce(lambda x, y: x*y, filter(lambda num: is_prime(num), xrange(1, limit+1)))

for divisible_num in itertools.count(step, step):
	if is_divisible(divisible_num, limit):
		break

print divisible_num
