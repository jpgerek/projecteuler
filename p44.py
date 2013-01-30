from itertools import count
from euler import pentagonal, is_pentagonal


result = ()

for n in count(1):
	pentagon_n = pentagonal(n)
	for sub_n in xrange(1, n):
		pentagon_sub_n = pentagonal(sub_n) 
		pentagon_diff = pentagon_n - pentagon_sub_n
		if is_pentagonal(pentagon_diff):
			pentagon_sum = pentagon_n + pentagon_sub_n
			if is_pentagonal(pentagon_sum):
				result = (pentagon_diff, n, sub_n, pentagon_n, pentagon_sub_n, pentagon_sum)
				break
	else:
		continue
	break

print "D: %d, n: %d, sub_n: %d, pentagon_n: %d, pentagon_sub_n: %d, pentagon_sumb: %d" % result