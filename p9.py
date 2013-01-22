import math
sum_abc = 1000
a_limit = sum_abc / 3
bc_limit = sum_abc / 2
print [reduce(lambda x, y: x*y, (a, b, c)) for (a, b, c) in ((a, b, c) for a in xrange(3, a_limit) for b in xrange(a+1, bc_limit) for c in xrange(b+1, bc_limit) if a+b+c == sum_abc) if a*a + b*b == c*c][0]
