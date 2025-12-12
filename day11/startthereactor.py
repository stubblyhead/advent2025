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

def get_all_descendents(tree, start, descendents):
    if start in descendents:
        return
    
    descendents.append(start)
    if not tree[start].get_children():
        return
    else:
        for child in tree[start].get_children():
            get_all_descendents(tree, child, descendents)

    return descendents

def get_all_ancestors(tree, start, ancestors):
    if start in ancestors:
        return
    
    ancestors.append(start)
    if not tree[start].get_parents():
        return
    else:
        for parent in tree[start].get_parents():
            get_all_ancestors(tree, parent, ancestors)

    return ancestors

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

    # with open('testcase2') as f:
    #     lines_part2 = f.readlines()

    lines_part2 = list(lines)

    nodestmp = parse_lines(lines_part2)
    nodes = build_tree(nodestmp)

    fft_children = get_all_descendents(nodes, 'fft', [])
    dac_children = get_all_descendents(nodes, 'dac', [])

    dac_ancestors = get_all_ancestors(nodes, 'dac', [])
    fft_ancestors = get_all_ancestors(nodes, 'fft', [])

    if len(dac_children) > len(fft_children) and len(dac_ancestors) < len(fft_ancestors):
        # dac is higher in tree than fft

        nodes_to_remove = []
        for node in nodes.keys():
            if (node in dac_children and \
                (node in fft_ancestors or node in fft_children)) \
                or \
                (node in fft_ancestors) and \
                (node in dac_ancestors or node in dac_children):
                continue
            else:
                nodes_to_remove.append(node)
        for node in nodes_to_remove:
            nodes.pop(node)

    else:
        # fft is higher
        nodes_to_remove = []
        for node in nodes.keys():
            if (node in fft_children and \
                (node in dac_ancestors or node in dac_children)) \
                or \
                (node in dac_ancestors) and \
                (node in fft_ancestors or node in fft_children):
                continue
            else:
                nodes_to_remove.append(node)
        for node in nodes_to_remove:
            nodes.pop(node)

    for nodeobj in nodes.values():
        parents_to_remove = []
        for p in nodeobj.get_parents():
            if p not in nodes.keys():
                parents_to_remove.append(p)
        for p in parents_to_remove:
            nodeobj.parents.remove(p)
        children_to_remove = []
        for c in nodeobj.get_children():
            if c not in nodes.keys():
                children_to_remove.append(c)
        for c in children_to_remove:
            nodeobj.children.remove(c)

    # I think after this all routes must go through dac and fft

    print(traverse(nodes,'svr'))
