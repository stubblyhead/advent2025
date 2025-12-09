from math import sqrt
from itertools import combinations

class Box:
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z

def get_distance(one, other):
    return sqrt((one.x - other.x)**2 + (one.y - other.y)**2 + (one.z - other.z)**2)


if __name__ == '__main__':
    with open('input') as f:
        lines = f.readlines()

    boxes = []
    circuits = []
    distances = []

    for l in lines:
        x,y,z = l.split(',')
        boxes.append(Box(int(x),int(y),int(z)))
        # honestly a circuits object will prbably be more trouble than it's worth
        # circuits.append(Circuit([boxes[-1]]))
        circuits.append([boxes[-1]])
    
    for i in combinations(boxes,2):
        distances.append((get_distance(*i),i))
    distances.sort()

    print(len(distances))

    for _ in range(1000):
        this_dist = distances.pop(0)
        box_a, box_b = this_dist[1]
        connect = []
        while len(connect) != 2:
            for i in range(len(circuits)):
                if box_a in circuits[i]:
                    connect.append(i)
                if box_b in circuits[i]:
                    connect.append(i)
            if connect[0] == connect[1]:
                break
            new_curcuit = circuits[connect[0]] + circuits[connect[1]]
            circuits = circuits[0:connect[0]] + circuits[connect[0]+1:connect[1]] + circuits[connect[1]+1:] + [new_curcuit]
    circuits.sort(key=len, reverse=True)
    prod = 1
    for i in range(3):
        prod *= len(circuits[i])

    print(prod)

    while distances:
        this_dist = distances.pop(0)
        box_a, box_b = this_dist[1]
        connect = []
        while len(connect) != 2:
            for i in range(len(circuits)):
                if box_a in circuits[i]:
                    connect.append(i)
                if box_b in circuits[i]:
                    connect.append(i)
            if connect[0] == connect[1]:
                break
            new_curcuit = circuits[connect[0]] + circuits[connect[1]]
            circuits = circuits[0:connect[0]] + circuits[connect[0]+1:connect[1]] + circuits[connect[1]+1:] + [new_curcuit]
        if len(circuits) == 1:
            break
    print(box_a.x * box_b.x)

