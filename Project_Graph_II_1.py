#####################################
##
## Submission of Mini project
##
##    Part II
##
#####################################

from Project_Graph_Classes import Node, Graph
from Project_Graph_I_1 import BuildNodes
import copy

MyNodes = BuildNodes() # build the nodes in graph in the project


##############################
## Question 1
##
## Creating 3 graph objects and then merge them By __add__()
##############################

MyGraph = [Graph("FirstSubGraph", MyNodes[0:3]),
           Graph("SecondSubGraph", MyNodes[3:8]),
           Graph("ThirdSubGraph", MyNodes[8:10])
           ]

print "*** Output for question 1 ***"
for i in xrange(0,2):
    print "Graph number %s" % i
    print MyGraph[i]

# Merge the graphs
MyFullGraph = MyGraph[0].__add__(MyGraph[1])
MyFullGraph = MyFullGraph.__add__(MyGraph[2])

print "The merged graph is:"
print MyFullGraph


##########################
## Testing of the various methods
##########################
### Test the contains function in all four cases

MyGraphX = copy.deepcopy(MyGraph[1])

print "\n\n ***** Test contains function ****"
for NodeName in ["5", "3"]:
    print "Check with node name: ", NodeName, " is in graph ", MyGraphX.__contains__(NodeName)
for NodeInstance in [MyNodes[4], MyNodes[2]]:
    print "Check with node instance: ", NodeInstance.name, " is in graph ", MyGraphX.__contains__(NodeInstance)


### Test getitem
print "\n\n ***** Test getitem function ****"

for NodeName in ["5", "3"]:
    try:
        NodeInstance = MyGraphX.__getitem__(NodeName)
    except KeyError:
        print "Node ", NodeName, " raised KeyError, in graph ", MyGraphX.name
        continue

    print "getitem in graph ", MyGraphX.name, " returned ", NodeInstance.name

print "\n***** End of tests"

### Test update graph

print "***** test update graph ****\n\nGraph Before Update"
print MyGraph[2]
print "\nAdd a new node\n"
print MyNodes[1]
MyGraph[2].update(MyNodes[1])
print "Updated graph"
print MyGraph[2]

print "***** test update graph ****\n\nGraph Before Update as above\nupdate node instance"
TempNode = copy.deepcopy(MyNodes[1])
TempNode.update("12", 11)
print "\nExisting node to be updated is:"
print TempNode

MyGraph[2].update(TempNode)
print "\nUpdated graph is"
print MyGraph[2]


print "***** test add two graphs ****\n\nGraphs are:"
print MyGraph[0], MyGraph[2]

print "\nMerged graph is"
FullGraph = MyGraph[0].__add__(MyGraph[2])
print FullGraph


##################
# Test remove node
print "***** test remove node ****\n\nGraph Before Remove: "
print MyGraphX


print "\nRemove node %s and Updated graph is" % MyNodes[5].name
MyGraphX.remove_node(MyNodes[5].name)
print MyGraphX

# Remove non existing node
print "\nRemove non existing node %s and Updated graph is" % MyNodes[5].name
MyGraphX.remove_node(MyNodes[5].name)
print MyGraphX

#########################
# Test is_edge
print "Testing is_edge?"
print "Is 4 edge of 3? (edge exists) ", FullGraph.is_edge('3', '4')
print "Is 1 edge of 9? (nodes exist but no edge) ", FullGraph.is_edge('9', '1')
print "Is 15 edge of 2? (node does not exist) ", FullGraph.is_edge('2', '15')

#########################
# Test add_edge

print "Add edge 4 to 2 (11) "
MyFullGraph.add_edge("4","2",11)
print "Add edge 4 to 11 (12) "
MyFullGraph.add_edge("4","11",12)
print "Full graph after adding 2 edges", MyFullGraph

#########################
# Test remove_edge
print "***** Test remove edge"
print "Remove 11 from 4"
MyFullGraph.remove_edge("4","11")
print "remove 11 again from 4"
MyFullGraph.remove_edge("4","11")
print "Full graph after removal", MyFullGraph


# rebuild full graph
MyNodes = BuildNodes()  # build the nodes in graph in the project
MyFullGraph = Graph("MyFullGraph", MyNodes[0:10])

print "***** Test get edge weight"
print "get edge weight 5 -> 6", MyFullGraph.get_edge_weight("5", "6")
print "get edge weight 4 -> 7", MyFullGraph.get_edge_weight("4", "7")
print "get edge weight 14 -> 6", MyFullGraph.get_edge_weight("14", "6")

print "***** Test get path weight"
print "null path weight", MyFullGraph.get_path_weight([])
print "Weight of 4 5 6", MyFullGraph.get_path_weight(['4', '5', '6'])
print "weight of 1 6 5", MyFullGraph.get_path_weight(['1', '6', '5'])

#########################
# Test is_reachable
print "**** Test is reachable"

print "Is reachable 9 1 ?", MyFullGraph.is_reachable('9', '1')
print "Is reachable 8 6 ?", MyFullGraph.is_reachable('8', '6')
print "Is reachable 9 6 ?", MyFullGraph.is_reachable('9', '6')
print "Is reachable 2 6 ?", MyFullGraph.is_reachable('2', '6')
print "Is reachable 6 2 ?", MyFullGraph.is_reachable('6', '2')

#########################
# Test Find shortest
print "Shortest 9 2 ?", MyFullGraph.find_shortest_path('9', '2')
print "Shortest 9 6 ?", MyFullGraph.find_shortest_path('9', '6')
print "Shortest 6 2 ?", MyFullGraph.find_shortest_path('6', '2')

print "End of tests"

#######################################
### Question #3
#######################################
ReachableCount = {}
for f in MyFullGraph.nodes:
    ReachableCount[f]=0
    for t in MyFullGraph[f].neighbors:
        if MyFullGraph.is_reachable(f, t): ReachableCount[f] = ReachableCount[f] + 1

print "\n***** Question #3\nNodes in ascending order by their reachable count"
print sorted(ReachableCount, key=lambda x: ReachableCount[x])


#######################################
### Question #4
#######################################
HighestWeight = ('', '', 0) # Shortest  from, to, weight
# Find all paths with their weights
for f in MyFullGraph.nodes:

    for t in MyFullGraph[f].neighbors:
        p, Shortest = MyFullGraph.find_shortest_path(f, t)
        if Shortest > HighestWeight[2]:
            HighestWeight = (f, t, Shortest)

print "\n***** Question #4\n"
print ("The shortest path with the highest weight is from {} to {}, and its weight is {}".format
       (HighestWeight[0], HighestWeight[1], HighestWeight[2]))







