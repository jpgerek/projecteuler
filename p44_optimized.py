from itertools import count, takewhile
from euler import pentagonal, is_pentagonal


result = ()
pentagonals_generated = set()

for n in count(1):
	pentagon_n = pentagonal(n)
	pentagonals_generated.add(pentagon_n)
	for pentagon_sub_n in takewhile(lambda p_sub_n: p_sub_n < pentagon_n, pentagonals_generated):
		pentagon_diff = pentagon_n - pentagon_sub_n
		if pentagon_diff in pentagonals_generated:
			pentagon_sum = pentagon_n + pentagon_sub_n
			if is_pentagonal(pentagon_sum):
				result = (pentagon_diff, n, pentagon_n, pentagon_sub_n, pentagon_sum)
				break
	else:
		continue
	break

print "D: %d, n: %d, pentagon_n: %d, pentagon_sub_n: %d, pentagon_sumb: %d" % result