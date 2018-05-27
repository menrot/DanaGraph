from Project_Graph_Classes import Node, Graph

Nodes = [] # create a list whose members will be the nodes
for i in range(0,5):
	Nodes.append(Node(str(i)))

# Now add the neighbors
Nodes[0].update('1', 10)
Nodes[0].update('2', 20)
Nodes[0].update('3', 30)

Nodes[1].update('4', 10)
Nodes[2].update('4', 5)


MyGraph = Graph("Graph", Nodes[0:5])

print MyGraph.find_all_paths('0','4')



