import math
from euler import is_prime, gen_primes

LIMIT = 10**6
primes_list = list(gen_primes(LIMIT))
primes_set = set()

start_offset = 0
end_offset = 0
cons_primes = []
nums_sum = 0
largest_cons_primes = []
while True:
	try:
		current_prime = primes_list[end_offset]
	except IndexError:
		start_offset += 1
		if start_offset > len(primes_list):
			break
		end_offset = start_offset
		cons_primes = []	
		nums_sum = 0
	cons_primes.append(current_prime)
	nums_sum += current_prime
	if nums_sum > LIMIT:
		start_offset += 1
		end_offset = start_offset
		cons_primes = []
		nums_sum = 0
		continue
	if is_prime(nums_sum) and len(cons_primes) > len(largest_cons_primes):
		largest_cons_primes = list(cons_primes)
	end_offset += 1	

print sum(largest_cons_primes)