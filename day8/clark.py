from math import sqrt
from itertools import combinations

class Box:
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z

def get_distance(one, other):
    return sqrt((one.x - other.x)**2 + (one.y - other.y)**2 + (one.z - other.z)**2)

class Circuit:
    def __init__(self, lights=[]):
        self.boxes = lights

    def add(self, other):
        return Circuit(self.lights + other.lights)
    
    def contains(self, box):
        return box in self.boxes
    
    def get_box_count(self):
        return len(self.boxes)
    
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