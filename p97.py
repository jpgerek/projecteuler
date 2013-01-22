print (28433*2**7830457+1) % 10**10

#-- other option --#
"""
last_digits = 1
for n in xrange(1,7830457+1):
	last_digits = last_digits * 2 % 10**10
last_digits = (28433*last_digits+1) % 10**10
print last_digits	
"""
