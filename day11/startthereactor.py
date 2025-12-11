class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def get_children(self):
        return self.children
    
    def has_child(self, child):
        return child in self.children
    
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

if __name__ == '__main__':

    with open('testcase') as f:
        lines = f.readlines()

    nodestmp = {}
    for l in lines:
        src,dst = l.split(': ')
        nodestmp[src] = dst.split()

    nodes = {}
    for n in nodestmp.keys():
        nodes[n] = Node(n)

    for k,v in nodestmp.items():
        for c in v:
            nodes[k].add_child(c)

    print(traverse(nodes, 'you'))