from graph_tool.all import *
from startthereactor import *

if __name__ == '__main__':

    with open('testcase') as f:
        lines = f.readlines()

    nodestmp = parse_lines(lines)
    
    reactor = Graph(directed=True)
    node_labels = reactor.new_vertex_property('string')
    nodes = {}
    edges = {}

    for n in nodestmp.keys():
        nodes[n] = reactor.add_vertex()
        node_labels[nodes[n]] = graph_draw(reactor)



