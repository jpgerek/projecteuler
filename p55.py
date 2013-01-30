from euler import is_palindromic

NUM_THRESHOLD = 10000

def is_lychrel(number, max_iterations=50):
	tmp_number = number
	for iteration in xrange(1, max_iterations+1):
		tmp_number += int(str(tmp_number)[::-1])
		if is_palindromic(tmp_number):
			return False
	return True

print len([number for number in xrange(NUM_THRESHOLD) if is_lychrel(number)])