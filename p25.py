import math
import itertools
from euler import fibonacci

def fib_term(n):
	phi = (1+math.sqrt(5))/2
	return round(math.pow(phi, n)/math.sqrt(5))

for offset, num in enumerate(fibonacci()):
	length = len(str(num))
	if length >= 1000:
		print offset+1
		break