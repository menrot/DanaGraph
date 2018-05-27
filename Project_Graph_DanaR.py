###################################
#
# Project Graph 
#
# Dana Rothschild
#
###################################

#### 
#### Classes for the project 
####

## Node in a direcetd graph
##  name - string
##  neighbors - dictionary of name: weight
##

import copy

class Node:

    def __init__(self, name):
        self.name = name
        self.neighbors = {}
        return(None)

    def __str__(self):
        return "Node name " + str(self.name) + " Neighbors: " + str(self.neighbors)

    def __len__(self):
        # returns the number of neighbors
        return (len(self.neighbors))

    def __contains__(self, item):
        # returns whether item is a name of a neighbor of self.
        try:
            self.neighbors[item]
            return(True)
        except:
            return(False)

    def __getitem__(self, item):
        # returns the weight of the neighbor named key.
        # If there is no such neighbor, then the method returns None
        try:
            return(self.neighbors[item])
        except:
            return(None)

    def __eq__(self, other):
        # based on the name attribute
        try:
            if self.name == other.name:
                return(True)
            else:
                return(False)
        except:
            return(False)

    def __ne__(self, other):
        # based on the name attribute
        try:
            if self.name != other.name:
                return(True)
            else:
                return(False)
        except:
            return(False)

    def is_neighbor(self,name):
        # equivalent to __contains__()
        return(self.__contains__(name))

    def update(self, name, weight):
        # adds name as a neighbor of self
        #   If name is not a neighbor of self, then it should be added
        #   If name is already a neighbor of self,
        #       then its weight should be updated to the maximum between the existing weight and weight
        #   This method should not allow adding a neighbor with the same name as self
        if self.name == name:
            return(False)   # can not add self as neighbor
        if self.__contains__(name):
            self.neighbors[name] = max(weight, self.neighbors[name]) #already a neighbor - update weight
        else:
            self.neighbors.update({name:weight}) # add new neighbor
        return(True)

    def remove_neighbors(self, name):
        # removes name from being a neighbor of self
        if name in self.neighbors:
            del self.neighbors[name]
        else:
            return(None)

    def is_isolated(self):
        # returns True if self has no neighbors
        if self.__len__() == 0:
            return(True)
        else:
            return(False)

## Graph is a direcetd graphs based on Node
##
##
##
##
class Graph:
    def __init__(self, name, nodes=[]):
        # nodes is an iterable of Node instances
        self.name = name
        self.nodes = {}
        for i in xrange(0, len(nodes)):
            self.nodes.update({nodes[i].name:nodes[i]})
        return(None)

    def __str__(self):
        # print the description of all the nodes in the graph
        returnStr = "\ngraph name: " + str(self.name) + "\n\tNodes: "
        for i in self.nodes:
            returnStr += "\n\t" + str(self.nodes[i])
        return returnStr

    def __len__(self):
        # returns the number of nodes in the graph
        return len(self.nodes)

    def __contains__(self, key):
        # returns True in two cases:
        #   (1) If key is a string, then if a node called key is in self
        #   (2) If key is a Node, then if a node with the same name is in self
        if isinstance(key, basestring): # key is a node name
            if key in self.nodes:
                return True
            else:
                return False
        elif isinstance(key, Node): # key is a Node, extract the Node.name attribute
            if key.name in self.nodes:
                return True
            else:
                return False

    def __getitem__(self, name):
        # returns the Node object whose name is name
        # raises KeyError if name is not in the graph.
        for k in self.nodes:
            if self.nodes[k].name == name:
                return self.nodes[k]
            continue
        # name not found
        raise KeyError

    def update (self, node):
        # adds a new node to the graph
        # node is a Node instance
        if not(self.__contains__(node)):
            # it is a new node
            self.nodes.update({node.name: node})
        else:
            # exiting node
            for n in node.neighbors: # node is in graph. Update its neighbor list
                self.nodes[node.name].update(n, node.neighbors[n])

        return

    def __add__(self, other):
        # returns a new Graph object that includes all the nodes and edges of self and other
        Merged = copy.deepcopy(self) # create a new graph
        for k in other.nodes: # iterate over all nodes of the other graph, and add/update each node
            Merged.update(other.nodes[k])
        return Merged

    def remove_node (self, node):
        # removes the node name from self
        # This method should not fail if name is not in self
        # This method should not remove edges,
        #   Austiin which name is a neighbor of other nodes in the graph.
        self.nodes.pop(node, None) # None assures no failure if node.name does not exist
        return

    def is_edge(self, frm_name, to_name):
        # returns True if to_name is a neighbor of frm_name.
        # This method should not fail if either frm_name or to_name is not in self.
        if self.__contains__(frm_name):
            if self.nodes[frm_name].is_neighbor(to_name):
                return(True)
        return(False)

    def add_edge(self, frm_name, to_name, weight):
        # adds an edge making to_name a neighbor of frm_name.
        #   This method applies the same logic as Graph.update().
        #   This method should not fail if either frm_name or to_name are not in self.
        if self.__contains__(frm_name):
            # frm_name is in graph. Update the relevant node in th egraph
            self.nodes[frm_name].update(to_name, weight)
        else:
            # from is not in Graph
            # Create a new Node with its neighbor list
            self.update(Node(frm_name,{to_name, weight}))
        return

    def remove_edge(self, frm_name, to_name):
        # removes to_name from being a neighbor of frm_name.
        #   This method should not fail if frm_name is not in self.
        #   This method should not fail if to_name is not a neighbor of frm_name.
        if self.__contains__(frm_name):
            self.nodes[frm_name].remove_neighbors(to_name)
        return

    def get_edge_weight(self, frm_name, to_name):
        # returns the weight of the edge between frm_name and to_name
        #   This method should not fail if either frm_name or to_name are not in self.
        #   This method should return None if to_name is not a neighbor of frm_name.
        if self.__contains__(frm_name):
            try:
                return self.nodes[frm_name].__getitem__(to_name) # if to_name does not exist - returns None
            except KeyError:
                return None
        return None

    def get_path_weight(self, path):
        # returns the total weight of the given path, where path is an iterable of nodes' names
        #   This method should return None if the path is not feasible in self.
        #   This method should return None if path is an empty iterable.
        #   Tip: The built-in functions any() and all() regard nonzero numbers as True and None as False.
        Total = 0
        ## if [all(x) for x in Graph[path]
        if len(path) == 0:
            return None
        for n in xrange(0,len(path)-1):
            x = self.get_edge_weight(path[n],path[n+1])
            if not(x):
                return None
            Total += x
        return Total

    def find_all_paths(self, frm_name, to_name, path=[], AllPath=True):
        # Returns a list of paths (each path is a list by itself) from frm_name to to_name
        path = path + [frm_name]
        if frm_name == to_name: # end of recursion - return
            return [path]
        if not (self.__contains__(frm_name)): # error condition
            return []
        paths = []
        for n in self[frm_name].neighbors:
            if n not in path:
                full_paths = self.find_all_paths(n, to_name, path)
                for p in full_paths:
                    paths.append(p)
                    if not(AllPath):
                        return paths # one path found
        return paths

    def is_reachable(self, frm_name, to_name):
        # returns True if to_name is reachable from frm_name.
        #   This method should not fail if either frm_name or to_name are not in self.
        if frm_name == to_name:
            return True
        if not(self.__contains__(frm_name)):
            return False

        paths = self.find_all_paths(frm_name, to_name)
        if len(paths) > 0:
            return True
        else:
            return False


    def find_shortest_path(self, frm_name, to_name):
        # returns the path from frm_name to to_name which has the minimum total weight,
        #   and the total weight of the path
        #   If not reachable retuen [], 0
        all_paths = [([],0)]
        if frm_name == to_name:
            return all_paths[0][0], all_paths[0][1]
        if not(self.__contains__(frm_name)):
            return all_paths[0][0], all_paths[0][1]

        paths = self.find_all_paths(frm_name, to_name)

        for p in paths:
            all_paths.append((p, self.get_path_weight(p)))

        all_paths = sorted(all_paths, key=lambda path_desc: path_desc[1]) # sort by weight
        if len(all_paths)>1: # path found
            return all_paths[1][0], all_paths[1][1]
        else: # no path found
            return all_paths[0][0], all_paths[0][1]

    def find_all_paths(self, frm_name, to_name, path=[]):
        path = path + [frm_name]
        if frm_name == to_name:
            return [path]
        if not (self.__contains__(frm_name)):
            return []
        paths = []
        for vertex in self[frm_name].neighbors:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex,
                                                     to_name,
                                                     path)
                for p in extended_paths:
                    paths.append(p)
        return paths


#####################################
##
## Part I
##
#####################################


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
print " ********** Part I task 1"
print " ********** Question #1 ********"
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

#####################################
##
##    Part II
##
#####################################

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



#####################################
##
##
##    Part II - Task 2
##
#####################################

import csv
from datetime import  datetime, timedelta

def interpret_csv(filename):
	#
	# Read a CSV file describing roads
	#
	# The function supports two formats of date and time
	# The output is the dictionary Edges:
	#		{From, {'to', [total travel time, num of travels]}}
	#
    Nodes1 = {'Center': Node('Center'), 'North': Node('North'), 'South': Node('South'),
              'East': Node('East'), 'West': Node('West')}
    Edges = { } # {From, {'to', [total travel time, num of travels]}}
    with open(filename, 'rb') as csvfile:
        travel = csv.reader(csvfile, delimiter=',')
        for row in travel:
            if (len(row) == 4):	# all 4 fields exist
                if row[0] in Nodes1: # is it a valid region? 
                    if row[1].find('M') < 0: #identify the format of the date and time
                        try:
                            StartTime = datetime.strptime(row[1], "%d/%m/%Y %Hh%Mm")
                            EndTime = datetime.strptime(row[3], "%d/%m/%Y %Hh%Mm")
                        except ValueError: # handle wrong data
                            print 'Exception ValeError ', row
                            continue
                    else:
                        # AM format
                        try:
                            StartTime = datetime.strptime(row[1], "%I:%M:%S%p ; %b %d %y")
                            EndTime = datetime.strptime(row[3], "%I:%M:%S%p ; %b %d %y")
                        except ValueError:
                            print 'Exception ValeError ', row
                            continue

                    DeltaTime = timedelta.total_seconds(EndTime - StartTime)
                    if row[0] in Edges:
                        # Update List of roads
                        Roads = Edges[row[0]]
                        if row[2] in Roads:
                            TotalTime = Roads[row[2]][0] + DeltaTime
                            TotalTravels = Roads[row[2]][1] + 1
                            Roads[row[2]][0] = TotalTime
                            Roads[row[2]][1] = TotalTravels
                        else:
                            # add new road
                            Roads[row[2]] = [DeltaTime, 1]
                        Edges[row[0]] = Roads
                    else:
                        # new From node
                        R = {}
                        R[row[2]] = [timedelta.total_seconds(EndTime - StartTime), 1]
                        Edges[row[0]] = R
            else:
                print 'missing info ', row
    return Edges

file_list = ['travelsEW.csv', 'travelsWE.csv']

graph=[]
for f in xrange(0, len(file_list)):

    Edges = interpret_csv(file_list[f])
    graph.append(Graph(file_list[f]))

    # Build the nodes
    for i in Edges:
        graph[f].update(Node(i))
        # Add the edges to each node
        for j in Edges[i]:
            graph[f].nodes[i].update(j,Edges[i][j][0]/Edges[i][j][1])


Roadmap = graph[0].__add__(graph[1]) # this is the graph including all nodew and roads

print "\n**** Task 3\nQuestion 1"
print "The roadmap is ", Roadmap

print "\nQuestion 2"

## Find the longest among the short paths between nodes
Longest = 0
for i in Roadmap.nodes:
    for j in Roadmap.nodes[i].neighbors:
        if Roadmap.nodes[i].neighbors[j] > Longest:
            Longest = Roadmap.nodes[i].neighbors[j]
            From = i
            To = j

print ("The longest time to travel takes from {} to {} and it takes {} seconds ".format(From, To, Longest))











