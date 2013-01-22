import itertools

def is_palindromic(num):
	str_num = str(num)
	return str_num == ''.join(reversed(str_num))

print max(a*b for a in xrange(100,1000) for b in xrange(100,1000) if is_palindromic(a*b))
