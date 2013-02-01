from pygraph.classes.digraph import digraph
from pygraph.algorithms.minmax import shortest_path
from pprint import pprint

f = open('matrix.txt')

matrix = [map(int, line.rstrip('\n').split(',')) for line in f.xreadlines()]

x_length = len(matrix[0])
y_length = len(matrix)

#- Creating gr -#
gr = digraph()

start_node = "start"
gr.add_node(start_node)
for x in xrange(x_length):
	for y in xrange(y_length):
		current_node = "%d,%d" % (x, y)
		current_node_weight = matrix[x][y]
		gr.add_node(current_node)
		if x > 0:
			left_node = "%d,%d" % (x-1, y)
			gr.add_edge((left_node, current_node), wt=current_node_weight)
		if y > 0:
			top_node = "%d,%d" % (x, y-1)
			gr.add_edge((top_node, current_node), wt=current_node_weight)

first_node_weight = matrix[0][0]
gr.add_edge((start_node, "0,0"), wt=first_node_weight)
last_node = "%d,%d" % (x_length-1, y_length-1)

tree, distances = shortest_path(gr, start_node)
print distances[last_node]