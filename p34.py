import math
result = []
UPPER_BOUND = 10**len(str(math.factorial(9)))
for num in xrange(3, UPPER_BOUND):
	digits_factorial_sum = sum(map(math.factorial, (int(digit_str) for digit_str in str(num))))
	if digits_factorial_sum == num:
		result.append(num)
print sum(result)		