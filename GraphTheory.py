from collections import deque 
'''
For the following problems involving graph theory i will be using a Graph class
and methods within to create a graph from given links and analyse the graphs
'''

'''
The graph_dictionary function will take in a set of tuples which will be the
two nodes on either end of the link

It will create a dictionary with each node as a key and the nodes it is linked
to as values
'''

def graph_dictionary(tuple_set):
    final = {}
    for el in tuple_set:
        if el[0] not in final:
            final.update({el[0]:[el[1]]})
        elif el[0] in final:
            final[el[0]] += el[1]
    return final

'''
dictionary_edges takes a graph dictionary and returns all edges as tuples of
each end of the edge
'''

def dictionary_edges(nodes):
    edges = []
    for node in nodes:
        for link in nodes[node]:
            new_edge = (node, link)
            edges.append(new_edge)
    return edges

def eulerian_path(new_graph):
    counter = 0
    path = []
    for node in new_graph:
        if len(new_graph[node]) %2 == 1:
            counter += 1
        elif len(new_graph[node]) == 0:
            print("One or more nodes on this graph are disconnected")
            return False
    if counter > 2:
        print("There is no Eulerian path")
        return False
    elif counter == 0:
        print("Here is an Eulerian cycle: ")
    elif counter == 2:
        print("There is no Eulerian cycle, here is an Eulerian path: ")
    stack = deque()
    stack.append({next(iter(new_graph)):new_graph[next(iter(new_graph))]})
    while True:
        current_vertex = list(stack[-1].keys())[0]
        if len(list(stack[-1].values())[0]) == 0:
            path.append(current_vertex)
            stack.pop()
        else:
            next_vertex = list(stack[-1].values())[0][0]
            new_graph[next_vertex].remove(current_vertex)
            new_graph[current_vertex].remove(next_vertex)
            stack.append({next_vertex:new_graph[next_vertex]})
            new_graph.update({current_vertex:new_graph[current_vertex]})
        if len(stack) == 0:
            break
    return path

print(graph_dictionary([('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'b'), ('c', 'a'),('a','d'),('d','a'),('c','f'),('f','c'),('f','d'),('d','f'),('a','c'),('c','a')]))
eulerian_path(graph_dictionary([('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'b'), ('c', 'a'),('a','d'),('d','a'),('c','f'),('f','c'),('f','d'),('d','f'),('a','c'),('c','a')]))