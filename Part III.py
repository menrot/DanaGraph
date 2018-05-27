from Project_Graph_Classes import Node, Graph


## NonDirectionalGraph is a graphs based on Node
##
# nondirectional graph is that its edges come in pairs.
#   when an edge is added or removed, the class makes
#   sure the same applies to its counterpart.

class NonDirectionalGraph(Graph):

    def add_edge(self, frm, to):
        # add an edge on both nodes
        super(NonDirectionalGraph, self).add_edge(frm, to)
        super(NonDirectionalGraph, self).add_edge(to, frm)

    def remove_edge(self, frm, to):
        # remove an edge from both ends
        super(NonDirectionalGraph, self).remove_edge(frm, to)
        super(NonDirectionalGraph, self).remove_edge(to, frm)

    def Count_Neighbors(self):
        # Count the total number of edges in the graph
        C = 0
        for n in self.nodes:
            C += len(self.nodes[n])
        return C/2  # each edge is counted twice, so has to adjust

    def maximal_path(self):

        LongestPathLength = 0
        ListOfNodes = []
        for n in self.nodes:
            ListOfNodes.append(n)

        for n in xrange(0,len(ListOfNodes)-1):
            for j in xrange(n+1, len(ListOfNodes)):
                # find all paths from n to j
                nName = ListOfNodes[n]
                jName = ListOfNodes[j]

                if nName <> jName: paths = self.find_all_paths(nName, jName)
            for k in xrange(0, len(paths)):
                LongestPathLength = max(LongestPathLength, len(paths[k])-1)
                if (len(paths[k])-1==LongestPathLength):
                    LongestPath = paths[k]
            if (LongestPathLength==len(ListOfNodes)-1):
                return LongestPathLength # This is the longest available
        return LongestPathLength


G1 = NonDirectionalGraph('testGraph')
G1.add_edge('a', 'b')
G1.add_edge('a', 'd')
G1.add_edge('b', 'd')
G1.add_edge('b', 'e')
G1.add_edge('e', 'f')
G1.add_edge('c', 'b')
G1.remove_edge('a', 'd')
G1.add_edge('d', 'f')

print G1
print G1.Count_Neighbors()


print G1.maximal_path()



SocialGraph = NonDirectionalGraph('social')

fname = 'social.txt'


MaxSimFriendship = 0
MaxSimReuben = 0
with open(fname) as f:
    # line = f.readlines()
    for line in f:
        words = line.split()
        if words[3] == "became":
            SocialGraph.add_edge(words[0], words[2])
        elif words [3] == 'cancelled':
            SocialGraph.remove_edge(words[0], words[2])
        # Count simultanous friendships
        CNeighbors = SocialGraph.Count_Neighbors()
        if CNeighbors > MaxSimFriendship:
            MaxSimFriendship = CNeighbors

        if (words[0]=='Reuben') or (words[2]=='Reuben'):
            MaxSimReuben = max(MaxSimReuben, len(SocialGraph.nodes['Reuben']))

print SocialGraph

print MaxSimFriendship

print MaxSimReuben

print SocialGraph.maximal_path()







