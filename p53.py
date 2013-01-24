import math

MIN_N = 1
MAX_N = 100
MIN_NUM = 10**6
R_LENGTH = 10
count = 0

def ncr(n, r):
	return math.factorial(n) / (math.factorial(r) * math.factorial(n-r))
	
for n in xrange(MIN_N, MAX_N+1):
	for r in xrange(MIN_N, n+1):
		if ncr(n, r) > MIN_NUM:
			count += 1

print count