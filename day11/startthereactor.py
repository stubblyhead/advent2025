class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parents = []

    def add_child(self, child):
        self.children.append(child)

    def add_parent(self, parent):
        self.parents.append(parent)

    def get_children(self):
        return self.children
    
    def get_parents(self):
        return self.parents
    
    def has_child(self, child):
        return child in self.children
    
    def has_parent(self, parent):
        return parent in self.parents
    
def traverse(tree, start):
    count = 0
    if start == 'out':
        return 1
    elif tree[start].get_children():
        for child in tree[start].get_children():
            count += traverse(tree,child)

    else:
        return 0
    
    return count

def build_tree(nodes):
    out = {}
    for n in nodes.keys():
        out[n] = Node(n)
    out['out'] = Node(out)
    
    for k,v in nodes.items():
        for c in v:
            out[k].add_child(c)
            out[c].add_parent(k)

    return out

def parse_lines(lines):
    out = {}
    for l in lines:
        src,dst = l.split(': ')
        out[src] = dst.split()
    return out

if __name__ == '__main__':

    with open('input') as f:
        lines = f.readlines()

    nodestmp = parse_lines(lines)
    nodes = build_tree(nodestmp)

    print(traverse(nodes, 'you'))

    with open('testcase2') as f:
        lines_part2 = f.readlines()

    # lines_part2 = list(lines)

    nodestmp = parse_lines(lines_part2)
    nodes = build_tree(nodestmp)