import itertools
count = 0
nums_list = []
for num in itertools.count(1):
	str_num = str(num)
	count += len(str_num)
	nums_list.append(str_num)
	if count > 1000000:
		break
nums = ''.join(nums_list)
print reduce(lambda a, b: a*b, (int(nums[0 if n == 0 else int('9'*n)]) for n in xrange(7)))