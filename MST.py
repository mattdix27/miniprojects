'''
Find the minimum spanning tree of a graph (subtree with minimum cost of edges)
'''

graph = { # initialise graph: 'starting node' : [list of {'ending node':length of edge}]
'a':[{'b':4},{'c':8},{'d':7},{'h':15}],
'b':[{'a':4},{'e':12}],
'c':[{'a':8},{'d':2},{'e':3}],
'd':[{'a':7},{'c':2},{'f':10},{'h':8}],
'e':[{'b':12},{'c':3},{'g':18}],
'f':[{'d':10},{'g':20},{'h':6}],
'g':[{'e':18},{'f':20},{'h':4}],
'h':[{'a':15},{'d':8},{'f':6},{'g':4},{'i':1},{'j':1},{'k':1}],
'i':[{'h':1},{'j':1},{'k':2}],
'j':[{'h':1},{'i':1},{'k':3}],
'k':[{'h':1},{'i':2},{'j':3}]
}


'''
create a list of all edges, sorted by their length as tuples of 3: start, end, length
'''
def edge_weights(graph):
    all_edges = []
    for node in graph:
        for edge in graph[node]:
            for key in edge:
                if (key, node, edge[key]) not in all_edges:
                    weighted_edge = (node, key, edge[key])
                    all_edges.append(weighted_edge)
    all_edges.sort(key=lambda x:x[2])
    return all_edges
        
def loop_check(end, tree, frontier, visited=[]):
    if tree == []:
        visited.clear()
        frontier.clear()
        return 0
    if len(frontier) == 0:
        visited.clear()
        frontier.clear()
        return 0
    if len(frontier) == len(tree):
        visited.clear()
        frontier.clear()
        return 0
    for edge in tree:
        if edge[0] in frontier and edge[1] not in visited and edge[1] not in frontier:
            frontier.append(edge[1])
        elif edge[1] in frontier and edge[0] not in visited and edge[0] not in frontier:
            frontier.append(edge[0])
    visited.append(frontier[0])
    frontier.remove(frontier[0])
    if end in frontier:
        visited.clear()
        frontier.clear()
        return 1
    else:
        return loop_check(end, tree, frontier, visited)
        
def MST(graph):
    tree = []
    edges = edge_weights(graph)
    for edge in edges:
        if loop_check(edge[1], tree, list(edge[0]))==0:
            tree.append(edge)
    return graph_dictionary(tree)

def graph_dictionary(tuple_set):
    final = {}
    for el in tuple_set:
        if el[0] not in final:
            final.update({el[0]:[el[1]]})
        elif el[0] in final:
            final[el[0]] += el[1]
        if el[1] not in final:
            final.update({el[1]:[el[0]]})
        elif el[1] in final:
            final[el[1]] += el[0]
    return final

print(MST(graph))