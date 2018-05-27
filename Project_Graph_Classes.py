#### 
#### Classes for the project 
####

## Node in a direcetd graph
##  name - string
##  neighbors - dictionary of name: weight
##

import copy

class Node(object):

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

    def update(self, name, weight=1):
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
class Graph(object):
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

    def add_edge(self, frm_name, to_name, weight=1):
        # adds an edge making to_name a neighbor of frm_name.
        #   This method applies the same logic as Graph.update().
        #   This method should not fail if either frm_name or to_name are not in self.
        if self.__contains__(frm_name):
            # frm_name is in graph. Update the relevant node in th egraph
            self.nodes[frm_name].update(to_name, weight)
        else:
            # from is not in Graph
            # Create a new Node with its neighbor list
            n =Node(frm_name)
            n.update(to_name, weight)
            self.update(n)
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




