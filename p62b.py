import itertools
import collections

PERMUTATIONS_NUM = 5
cubes_dict = collections.defaultdict(list)
for base in itertools.count():
	cube = base ** 3
	cube_key = ''.join(sorted([d for d in str(cube)]))
	cubes_list = cubes_dict[cube_key]
	cubes_list.append(cube)
	if len(cubes_list) == PERMUTATIONS_NUM:
		print min(cubes_list)
		break
