from collections import defaultdict
from heapq import heappush, heappop 
from math import sqrt

def prim(graph):
    """
    ### TODO:
    Update this method to work when the graph has multiple connected components.
    Rather than returning a single tree, return a list of trees,
    one per component, containing the MST for each component.

    Each tree is a set of (weight, node1, node2) tuples.    
    """
    def prim_helper(visited, frontier, tree):
        if len(frontier) == 0:
            return tree
        else:
            weight, node, parent = heappop(frontier)
            if node in visited:
                return prim_helper(visited, frontier, tree)
            else:
                print('visiting', node)
                # record this edge in the tree
                #tree.add((weight, node, parent))
                n1, n2 = sorted([node, parent])
                tree.add((weight, n1, n2))
                visited.add(node)
                for neighbor, w in graph[node]:
                    if neighbor not in visited:
                        heappush(frontier, (w, neighbor, node))    
                    # compare with dijkstra:
                    # heappush(frontier, (distance + weight, neighbor))                

                return prim_helper(visited, frontier, tree)
        
    # pick first node as source arbitrarily
    #source = list(graph.keys())[0]
    #frontier = []
    #heappush(frontier, (0, source, source))
    visited = set()  # store the visited nodes (don't need distance anymore)
    trees = []

    for node in list(graph.keys()):
        if node not in visited:
            frontier = []
            heappush (frontier, (0, node, node))
            tree = set()
            prim_helper(visited, frontier, tree)
            trees.append(tree)
    return trees

def mst_from_points(points):
    """
    Return the minimum spanning tree for a list of points, using euclidean distance 
    as the edge weight between each pair of points.
    See test_mst_from_points.

    Params:
      points... a list of tuples (city_name, x-coord, y-coord)

    Returns:
      a list of edges of the form (weight, node1, node2) indicating the minimum spanning
      tree connecting the cities in the input.
    """
    graph = defaultdict(list)

    for i in range(len(points)):
        for j in range(i+1, len(points)):
            p1 = points[i]
            p2 = points[j]

            city_name1= p1[0]
            city_name2= p2[0]

            weight = euclidean_distance(p1, p2)

            graph[city_name1].append((city_name2, weight))
            graph[city_name2].append((city_name1, weight))

    tree = prim(graph)
    return tree[0]


    ###TODO
    pass

def euclidean_distance(p1, p2):
    return sqrt((p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)

def test_euclidean_distance():
    assert round(euclidean_distance(('a', 5, 10), ('b', 7, 12)), 2) == 2.83
