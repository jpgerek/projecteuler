import itertools
print [''.join(map(lambda x: str(x), perm)) for offset, perm in enumerate(itertools.permutations(range(0,10))) if offset == (10**6)-1][0]
