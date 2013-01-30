import itertools
from euler import is_palindromic

print max(a*b for a in xrange(100,1000) for b in xrange(100,1000) if is_palindromic(a*b))
