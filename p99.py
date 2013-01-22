import math
f = open("base_exp.txt", "r")
higher_exp = 0.0
line_num = 0
higher_line_num = 0
for line in f.xreadlines():
	line_num += 1
	base, exp = map(int, line.split(','))
	new_exp = math.log(base)*exp
	if new_exp > higher_exp:
		higher_exp = new_exp
		higher_line_num = line_num
print higher_line_num
