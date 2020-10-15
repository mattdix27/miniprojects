import sys
'''
Graph with multiple nodes as well as edges with lengths

Find the shortest distance to any node
'''

graph = {
'a':[{'b':4},{'c':8},{'d':7}],
'b':[{'a':4},{'e':12}],
'c':[{'a':8},{'d':2},{'e':3}],
'd':[{'a':7},{'c':2},{'f':10}],
'e':[{'b':12},{'c':3},{'g':18}],
'f':[{'d':10},{'g':20}],
'g':[{'e':18},{'f':20}]
}

def minimum_distance(distances, visited): # find the node with the shortest distance
    min_distance = sys.maxsize
    for node in distances:
        if node in visited:
            continue
        if distances[node] < min_distance:
            min_distance = distances[node]
            min_node = node
    return min_node # return the key for the node/node identifier

def visiting(node,distances,visited):              # process for visiting each node
    for edge in graph[node]:
        edge_key=list(edge.keys())[0]              # letter of the other end of the edge
        edge_value=list(edge.values())[0]          # length of the edge to reach the other end
        new_total = distances[node] + edge_value   # adding the distance of current node to the length of the edge to visit
        if edge_key not in visited:
            if new_total < distances[edge_key]:    # replace if distances value is greater than new total
                distances.update({edge_key:new_total})
    visited.append(node)                           # add the current node to the visited list

def shortest(graph):
    distances = {} # this will be a dictionary of shortest distances to each node
    visited = []   # this is all nodes that have been completely visited
    
    for node in graph: # iterate through all nodes to make distance infinity
        distances.update({node:sys.maxsize})
    
    distances.update({next(iter(graph)):0}) # set distance of source to 0

    while len(visited) != len(graph):
        closest = minimum_distance(distances, visited)
        visiting(closest,distances,visited)
    
    print(visited)
    print(distances)

    
shortest(graph)