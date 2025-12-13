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
    
memo = {}
    
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

def get_routes_between_two_nodes(tree, start, end):
    if (start,end) in memo.keys():
        return memo[(start,end)]
    count = 0
    if start == end:
        return 1
    elif tree[start].get_children():
        for child in tree[start].get_children():
            count += get_routes_between_two_nodes(tree, child, end)
    else:
        return 0
    memo[start,end] = count
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
    result = {}
    for n in nodes.keys():
        result[n] = Node(n)
    result['out'] = Node('out')
    
    for k,v in nodes.items():
        for c in v:
            result[k].add_child(c)
            result[c].add_parent(k)

    return result

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

    print(get_routes_between_two_nodes(nodes, 'you', 'out'))

    # with open('testcase2') as f:
    #     lines_part2 = f.readlines()

    lines_part2 = list(lines)

    nodestmp = parse_lines(lines_part2)
    nodes = build_tree(nodestmp)

    fft_children = get_all_descendents(nodes, 'fft', [])
    dac_children = get_all_descendents(nodes, 'dac', [])

    dac_ancestors = get_all_ancestors(nodes, 'dac', [])
    fft_ancestors = get_all_ancestors(nodes, 'fft', [])

    # new approach -- if paths must go from svr to out through dac and fft,
    # then they must go from svr to the higher node in [dac, fft], from there
    # to the lower node in [dac, fft] and finally to out.  we can construct the
    # number of routes piecemeal by finding the count of each subroute and
    # multiplying together.

    if len(dac_children) > len(fft_children) and len(dac_ancestors) < len(fft_ancestors):
        # dac is higher in tree than fft

        svr_to_dac = get_routes_between_two_nodes(nodes, 'svr', 'dac')
        dac_to_fft = get_routes_between_two_nodes(nodes, 'dac', 'fft')
        fft_to_out = get_routes_between_two_nodes(nodes, 'fft', 'out')
        print(svr_to_dac*dac_to_fft*fft_to_out)

    else:
        # fft is higher
        dac_to_out = get_routes_between_two_nodes(nodes, 'dac', 'out')
        fft_to_dac = get_routes_between_two_nodes(nodes, 'fft','dac')
        svr_to_fft = get_routes_between_two_nodes(nodes, 'svr', 'fft')
        
        print(svr_to_fft*fft_to_dac*dac_to_out)
