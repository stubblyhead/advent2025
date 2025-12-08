from math import sqrt

class Box:
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def get_distance(self, other):
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)

class Circuit:
    def __init__(self, lights=[]):
        self.boxes = lights

    def add(self, other):
        return Circuit(self.lights + other.lights)
    
    def contains(self, box):
        return box in self.boxes
    
    def get_box_count(self):
        return len(self.boxes)