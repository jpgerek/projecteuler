import itertools

PERMUTATIONS_NUM = 5
cubes_list = []
bases_list = []
cubes_elements_list = []
first_base = 1
while True:
	for base in itertools.count(start=first_base):
		cube = base ** 3
		cube_elements = [d for d in str(cube)]
		cube_elements.sort() # We need it sorted to compared with other lists.
		cubes_list.append(cube)
		bases_list.append(base)
		cubes_elements_list.append(tuple(cube_elements))
		#- If it's the first cube continue to generate more -#
		if len(cubes_list) == 1:
			continue
		#- Comparing the last 2 cubes generated -#
		last_cube_elements = cubes_elements_list[-1]
		before_last_cube_elements = cubes_elements_list[-2]
		#- Checking if the last cube have more elements than the one before -#
		if len(before_last_cube_elements) < len(last_cube_elements):
			#- Making sure we start with the previous element incremented -#
			first_base = bases_list[-2]+1
			#- Deleting the last 2 bases tried -#
			cubes_list.pop()
			bases_list.pop()
			cubes_elements_list.pop()
			cubes_list.pop()
			bases_list.pop()
			cubes_elements_list.pop()
			break
		#- Checking if the last 2 cubes have the same elements -#
		if before_last_cube_elements != last_cube_elements:
			#- Last cubes wheren't a permutation of each other trying next -#
			cubes_list.pop()
			bases_list.pop()
			cubes_elements_list.pop()
			continue
		#- The permutations are equal and we got the amount we needed -#
		if len(cubes_list) == PERMUTATIONS_NUM:
			print 'Smallest cube: %d' % min(cubes_list)
			exit(0)