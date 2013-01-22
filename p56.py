MAX_B = 100
print max(map(lambda num: sum(int(c) for c in str(num)), set(str(a**b) for a in xrange(1, MAX_B+1) for b in xrange(1, MAX_B+1))))
