import itertools
import math

lst = []
for base in xrange(1, 10+1):
	for exp in xrange(1,30):
		power = base**exp
		length = len(str(power))
		if exp == length:
			lst.append((base, exp, length, power))
		if exp > length:
			break
print len(lst)
