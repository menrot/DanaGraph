
class Node:

    def __init__(self, name):
        self.name = name
        self.neighbors = {}
        return(None)

    def __str__(self):
        return "Node name " + str(self.name) + " Neighbors: " + str(self.neighbors)


    def __len__(self):
        return (len(self.neighbors))

    def __contains__(self, item):
        try:
            self.neighbors[item]
            return(True)
        except:
            return(False)

    def __getitem__(self, item):
        try:
            return(self.neighbors[item])
        except:
            return(None)

    def __eq__(self, other):
        try:
            if self.name == other.name:
                return(True)
            else:
                return(False)
        except:
            return(False)

    def __ne__(self, other):
        try:
            if self.name != other.name:
                return(True)
            else:
                return(False)
        except:
            return(False)

    def is_neighbor(self,name):
        return(self.__contains__(self, item))

    def update(self, name, weight):
        if self.name == name:
            return(False)
        if self.__contains__(name):
            self.neighbors[name] = max(weight, self.neighbors[name])
        else:
            self.neighbors.update({name:weight})
        return(True)

    def remove_neighbors(self, name):
        if name in self.neighbors:
            del self.neighbors[name]
        else:
            return(None)

    def is_isolated(self):
        if self.__len__() == 0:
            return(True)
        else:
            return(False)


MyGraph = Node("1")

MyGraph.update("2", 10)
MyGraph.update("4", 20)
MyGraph.update("5", 20)
MyGraph.update("6", 5)
MyGraph.update("7", 15)
MyGraph.update("8", 5)

print MyGraph


MyGraph = Node("2")

MyGraph.update("3", 5)
MyGraph.update("4", 10)

print MyGraph



