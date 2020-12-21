import re
from collections import defaultdict

lines = [l.strip().split(' contain ') for l in open("day7.txt").readlines()]

patt = re.compile('([0-9]+) ([a-z]+ [a-z]+) bag(?:s)?|(no other bags)')


class Graph():
    """Simple graph obj to work with Dijkstra's Algorithm"""
    def __init__(self):
        self.edges = defaultdict(list)
        self.weights = {}
        
    def add_edge(self, from_node, to_node, weight):
        """Add an edge to the graph in one direction: from_node -> to_node """
        self.edges[from_node].append(to_node)
        self.weights[(from_node, to_node)] = weight
        
    def dijkstra(self, initial, end):
        shortest_paths = {initial: (None, 0)}
        current_node = initial
        visited = set()
        
        while current_node != end:
            visited.add(current_node)
            destinations = self.edges[current_node]
            weight_to_current = shortest_paths[current_node][1]
            
            for next_node in destinations:
                weight = self.weights[(current_node, next_node)] + weight_to_current
                if next_node not in shortest_paths:
                    shortest_paths[next_node] = (current_node, weight)
                else:
                    current_shortest_weight = shortest_paths[next_node][1]
                    if current_shortest_weight > weight:
                        shortest_paths[next_node] = (current_node, weight)
            next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
            
            if not next_destinations:
                return False
            
            # next node is the destination with the lowest weight
            current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
            
        # work back through destinations in shortest path
        path = []
        while current_node is not None:
            path.append(current_node)
            next_node = shortest_paths[current_node][0]
            current_node = next_node
            
        # spin back flip it and reverse it
        return path[::-1]

d = defaultdict(dict)
g = Graph()
nodes = []

for outerBag, contains in lines:
    outerBag = outerBag.strip(' bags')
    if not outerBag in nodes:
        nodes.append(outerBag)
    obnode = nodes.index(outerBag)
    for match in patt.finditer(contains):
        if not 'no other bags' in match.groups():
            if not match.group(2) in nodes:
                nodes.append(match.group(2))
            conbag = nodes.index(match.group(2))

            g.add_edge(
                obnode,
                conbag,
                1/(int(match.group(1))**2)
            )
            d[outerBag][match.group(2)]=int(match.group(1))
        else:
            d[outerBag] = 0

count = 0
for i, n in enumerate(nodes):
    path = g.dijkstra(i, nodes.index('shiny gold'))
    if path:
        count += 1

print(f'A total of {count} bags can hold a shiny gold bag')