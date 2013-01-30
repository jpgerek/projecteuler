from euler import cf_sqrt

LIMIT = 10000

result = []
for n in xrange(1, LIMIT+1):
	cf_digits = cf_sqrt(n)
	if len(cf_digits) == 1:
		continue
	#- Removing the integer part -#
	cf_digits.pop(0)
	if len(cf_digits) % 2 == 1:
#		print (n, cf_digits)
		result.append((n, cf_digits))
		
print len(result)