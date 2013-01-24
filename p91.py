import math
import matplotlib.pyplot as plt
import time
MAX_COORD = 50

def points_distance((ax, ay), (bx, by)):
	return math.sqrt((ax - bx) ** 2 + (ay - by) ** 2)

def segments_form_right_triangle(a, b, c):
	leg1, leg2, hypotenuse = sorted((a, b, c))
	abs((leg1 ** 2) + (leg2 ** 2) - (hypotenuse ** 2)) < 0.1

origin = (0, 0)
triangles = set()
count = 0
for x1 in xrange(0, MAX_COORD+1):
	for y1 in xrange(0, MAX_COORD+1):
		#- Skipping the origin -#
		if x1 == y1 == 0:
			continue
		for x2 in xrange(0, MAX_COORD+1):
			for y2 in xrange(0, MAX_COORD+1):
				#- Skipping the origin -#
				if x2 == x2 == 0:
					continue
				#- Avoiding repeating the same point -#
				if x1 == x2 and y1 == y2:
					continue
				leg1, leg2, hypotenuse = sorted((points_distance((x1, y1), origin), points_distance((x2, y2), origin), points_distance((x1, y1), (x2, y2))))
				if segments_form_right_triangle(leg1, leg2, hypotenuse):
					#- Add only if there isn't another point of pairs but in different order -#
					if ((x2, y2), (x1, y1)) not in triangles:
						triangles.add(((x1, y1), (x2, y2)))
print len(triangles)