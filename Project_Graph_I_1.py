#####################################
##
## Submission of Mini project
##
## Part I
##
#####################################

from Project_Graph_Classes import Node


########################################
# Question #1
# Build the list of nodes
########################################
def BuildNodes():
	Nodes = [] # create a list whose members will be the nodes
	for i in range(1,11):
		Nodes.append(Node(str(i)))

	# Now add the neighbors
	Nodes[0].update("2", 10)
	Nodes[0].update("4", 20)
	Nodes[0].update("5", 20)
	Nodes[0].update("6", 5)
	Nodes[0].update("7", 15)
	Nodes[0].update("8", 5)

	Nodes[1].update("3", 5)
	Nodes[1].update("4", 10)

	Nodes[2].update("2", 15)
	Nodes[2].update("4", 5)

	Nodes[3].update("5", 10)

	Nodes[4].update("6", 5)

	Nodes[5].update = Node("6")

	Nodes[6].update("6", 10)

	Nodes[7].update("1", 5)
	Nodes[7].update("2", 20)

	Nodes[8].update("2", 15)
	Nodes[8].update("10",10)
	Nodes[8].update("8", 20)

	Nodes[9].update("2", 5)
	Nodes[9].update("3", 15)

	return Nodes


###########

MyNodes = BuildNodes() # Build the nodes described in the project

# Print the nodes
print "The nodes of the graph are:"
for i in xrange(0, len(MyNodes)):
    print MyNodes[i]
print "End of nodes"

##################################################
# Question #2
# test some functions
##################################################
print
print " ********** Question #2 ********"
print "Is isolated?"
for i in xrange(0, len(MyNodes)):
    print MyNodes[i].name, " Isolated? ", MyNodes[i].is_isolated()

print
print "Is neighbor?"
for i in xrange(0, len(MyNodes)):
    print MyNodes[i].name, " is a neighbor od ", str(i+2)," ? ", MyNodes[i].is_neighbor(str(i+2))

##################################################
# Question #3
# Count the edges and their total weight
##################################################
print
print " ********** Question #3 ********"
print "Count of edges and total weight"
NumberOfEdges = 0
WeightOfEdges = 0
for i in xrange(0, len(MyNodes)):
    for n in MyNodes[i].neighbors:
        NumberOfEdges += 1
        WeightOfEdges += MyNodes[i].neighbors[n]

print "Total Number of Edges is: ", NumberOfEdges, " Total weight of edges is ", WeightOfEdges

##################################################
# Question #4
# Sort the nodes by the number of their neighbors
##################################################
print
print " ********** Question #4 ********"
print " Sort the nodes by the number of their neighbors, Ascending"
SortedNodes = sorted(MyNodes, key=lambda node:len(node.neighbors))

for i in xrange(0, len(SortedNodes)):
    print SortedNodes[i]
print "End of nodes"

