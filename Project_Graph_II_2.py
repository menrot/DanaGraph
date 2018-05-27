#####################################
##
## Submission of Mini project
##
##    Part II - Task 2
##
#####################################

from Project_Graph_Classes import Node, Graph
import csv
from datetime import  datetime, timedelta

def interpret_csv(filename):
    Nodes1 = {'Center': Node('Center'), 'North': Node('North'), 'South': Node('South'),
              'East': Node('East'), 'West': Node('West')}
    Edges = { } # {From, {'to', [total travel time, num of travels]}}
    with open(filename, 'rb') as csvfile:
        travel = csv.reader(csvfile, delimiter=',')
        for row in travel:
            if (len(row) == 4):
                if row[0] in Nodes1:
                    if row[1].find('M') < 0:
                        try:
                            StartTime = datetime.strptime(row[1], "%d/%m/%Y %Hh%Mm")
                            EndTime = datetime.strptime(row[3], "%d/%m/%Y %Hh%Mm")
                        except ValueError:
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
                        # new From
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


Roadmap = graph[0].__add__(graph[1])

print "\n**** Task 3\nQuestion 1"
print "The roadmap is ", Roadmap

print "\nQuestion 2"

Longest = 0
for i in Roadmap.nodes:
    for j in Roadmap.nodes[i].neighbors:
        if Roadmap.nodes[i].neighbors[j] > Longest:
            Longest = Roadmap.nodes[i].neighbors[j]
            From = i
            To = j

print ("The longest time to travel takes from {} to {} and it takes {} seconds ".format(From, To, Longest))



