def is_inside_triangle((ax, ay), (bx, by), (cx, cy), (px, py)):
	plane_bc = (bx - px) * (cy - py) - (cx - px) * (by - py)
	plane_ab = (ax - px) * (by - py) - (bx - px) * (ay - py)
	plane_ca = (cx - px) * (ay - py) - (ax - px) * (cy - py)
	sign = lambda x: 1 if x > 0 else -1
	return sign(plane_ab) == sign(plane_bc) == sign(plane_ca)

triangles = []
f = open("triangles.txt")
for line in f.xreadlines():
	ax, ay, bx, by, cx, cy = map(int, line.split(','))
	if is_inside_triangle((ax, ay), (bx, by), (cx, cy), (0, 0)):
		triangles.append(((ax, ay), (bx, by), (cx, cy), (0, 0)))
print len(triangles)