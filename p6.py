limit=100
print sum(xrange(1, limit+1))**2 - sum(a*a for a in xrange(1, limit+1))
