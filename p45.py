import itertools

def triangle(n):
	return n*(n+1)/2

def pentagonal(n):
	return n*(3*n-1)/2

def hexagonal(n):
	return n*(2*n-1)

t_set = set()
p_set = set()
h_set = set()

start_nt = 285
start_np = 165
start_nh = 143

for n in itertools.count(1):
	cur_nt = start_nt + n
	cur_np = start_np + n
	cur_nh = start_nh + n
	tn = triangle(cur_nt)
	pn = pentagonal(cur_np)
	hn = hexagonal(cur_nh)
	t_set.add(tn)
	p_set.add(pn)
	h_set.add(hn)
	if n%10000 == 0:
		inter_set = t_set.intersection(p_set).intersection(h_set)
		if len(inter_set) != 0:
			print "result: %d" % inter_set.pop()
			break
