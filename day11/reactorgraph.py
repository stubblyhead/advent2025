from graph_tool.all import *
from startthereactor import *

if __name__ == '__main__':

    with open('input') as f:
        lines = f.readlines()

    nodestmp = parse_lines(lines)
    
    reactor = Graph(directed=True)
    node_labels = reactor.new_vertex_property('string')
    nodes = {}
    edges = {}
    node_colors = reactor.new_vertex_property('string')

    for n in nodestmp.keys():
        nodes[n] = reactor.add_vertex()
        node_labels[nodes[n]] = n
        if n in ['svr', 'you']:
            node_colors[nodes[n]] = '#1c71d8'
        elif n in ['fft','dac']:
            node_colors[nodes[n]] = '#2ec27e'
        else:
            node_colors[nodes[n]] = '#ff0000'
    nodes['out'] = reactor.add_vertex()
    node_labels[nodes['out']] = 'out'
    node_colors[nodes['out']] = "#b9b909"
    for k,v in nodestmp.items():
        for c in v:
            reactor.add_edge(source=nodes[k],target=nodes[c])
        
    graph_draw(reactor, vertex_fill_color=node_colors, vertex_text=node_labels, vertex_size=20)



