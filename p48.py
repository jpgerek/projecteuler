print reduce(lambda sum, x: sum+x,[x**x%10**10 for x in xrange(1,1000+1)])
