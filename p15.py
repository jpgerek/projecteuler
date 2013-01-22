import math
import itertools

def routes(width, height, x=0, y=0, cache={}):
	count_x = 0
	count_y = 0
	if x  >= width and y >= height:
		return 1
	cache_key = "%d-%d:%d-%d" % (width, height, x, y)
	if cache_key in cache:
		return cache[cache_key]
	if x < width:
		count_x = routes(width, height, x+1, y)
	if y < height:
		count_y = routes(width, height, x, y+1)
	count = count_x + count_y
	cache[cache_key] = count
	return count	

for side in xrange(1, 21):
	print "Side: %d -> %d" % (side, routes(side, side))