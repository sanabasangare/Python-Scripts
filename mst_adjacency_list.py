"""This algorithm finds the MST of an undirected graph by examining 
    all the edges and nodes, then stores only the edges with
    the smallest value with the connected nodes of that 
    edge if they have not already been added."""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.edges = []

class Edge(object):
    def __init__(self, data, parent, child):
        self.data = data
        self.parent = parent
        self.child = child

class Graph(object):
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_edge(self, new_edge_dt, parent_dt, child_dt):
        start = None
        stop = None
        for node in self.nodes:
            if parent_dt == node.data:
                parent_found = node
            if child_dt == node.data:
                stop = node
        if start == None:
            start = Node(parent_dt)
            self.nodes.append(start)
        if stop == None:
            stop = Node(child_dt)
            self.nodes.append(stop)
        new_edge = Edge(new_edge_dt, start, stop)
        start.edges.append(new_edge)
        stop.edges.append(new_edge)
        self.edges.append(new_edge)

def miN_spaN_treE(self):
    """This will return the edges with
        the smallest value as well as
        the connected nodes."""
    min_edges = sorted(self.edges, key=lambda edge: edge.data)
    adj_list = {}
    seen = []
    while len(min_edges) > 0:
        # this removes the "min_edges" index but still returns its value
        e = min_edges.pop(0)
        if e.parent.data not in seen or e.child.data not in seen:
            adj_list.setdefault(e.parent.data, []).append((e.child.data, e.data))
            seen.append(e.parent.data)
            seen.append(e.child.data)

    for edge in adj_list.keys():
        child_nodes = [i for i, j in adj_list[edge]]
        for n in child_nodes:
            if n in adj_list.keys():
                child_nodes2 = [i for i, j in adj_list[n]]
                if edge not in child_nodes2:
                    for i, j in adj_list[edge]:
                        if i == n:
                            val = j
                    adj_list[n].append((edge, j))
            else:
                for i, j in adj_list[edge]:
                    if i == n:
                        val = j
                adj_list[n] = [(edge, val)]
    return adj_list

g = Graph()
g.add_edge(9, 'A', 'B')
g.add_edge(5, 'B', 'C')
g.add_edge(3, 'C', 'B')
g.add_edge(4, 'C', 'A')

print miN_spaN_treE(g)
