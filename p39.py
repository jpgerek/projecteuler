import math
import collections

MAX_P = 1000

perimeters_dict = collections.defaultdict(int)
legs_dict = collections.defaultdict(list)
for perimeter in xrange(3, MAX_P+1):
	max_h = int(1 + (perimeter-1)**2) / (2 * (perimeter-1))
	min_h = int(perimeter/3) 	
	for hypotenuse in xrange(min_h, max_h+1):
		max_leg = hypotenuse -1
		min_leg = int(math.sqrt(hypotenuse**2 - max_leg**2))
		for leg1 in xrange(min_leg, max_leg):
			leg2 = perimeter - hypotenuse - leg1
			if (leg1 ** 2 + leg2 ** 2) == (hypotenuse ** 2):
				perimeters_dict[perimeter] += 1
				legs_dict[perimeter].append((leg1, leg2, hypotenuse))
				break
max_perimeter = max(perimeters_dict, key=lambda key: perimeters_dict[key])
print max_perimeter