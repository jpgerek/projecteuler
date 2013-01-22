def seq_len(num, cache={}):
	count = 0
	tmp_num = num
	while True:
		if tmp_num in cache:
			count += cache[tmp_num]
			break
		if tmp_num == 1:
			break
		if tmp_num%2 == 0:
			tmp_num = tmp_num/2
		else:
			tmp_num = 3*tmp_num + 1
		count += 1
	if num not in cache:
		cache[num] = count
	return count

print max(((num, seq_len(num)) for num in xrange(1,10**6)), key=lambda (a, b): b)[0]
