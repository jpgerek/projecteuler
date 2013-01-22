import math
import itertools
from euler import is_prime

count = 2
for num in itertools.count(3):
	num += 2
	if is_prime(num):
		count += 1
	if count == 10001:
		break	
print num