GOAL = 100

#- Based on http://taskinoor.wordpress.com/2011/11/20/the-relation-between-integer-partition-and-pentagonal-numbers/ -#     
def partitions_count(n):
	p = [1]
	for i in range(1, n + 1):
		s = 0
		k = 1
		while True:
			for sign in (-1, 1):
				f = i - k * (3 * k + sign) / 2
				if f < 0:
					break
				if k % 2:
					s += p[f]
				else:
					s -= p[f]
			else:
				k += 1
				continue
			break
		p.append(s)
	return p[-1]

#- I subtract one because it has to be the sum of at least two numbers so the case where the list is just the goal shouldn't count -#
print partitions_count(GOAL)-1