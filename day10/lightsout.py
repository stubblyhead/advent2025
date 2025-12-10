from itertools import combinations_with_replacement as cwr

class Light:
    def __init__(self):
        self.state = False

    def get_state(self):
        return self.state
    
    def toggle(self):
        self.state = not self.state

    def turn_on(self):
        if not self.get_state():
            self.toggle()

    def turn_off(self):
        if self.get_state():
            self.toggle()


class LightArray:
    def __init__(self,n):
        self.lights = [ Light() for _ in range(n) ]

    def press_button(self,btn):
        btn = list(map(int, btn[1:-1].split(',')))
        for b in btn:
            self.lights[b].toggle()

    def reset(self):
        for l in self.lights:
            l.turn_off() 

    def __repr__(self):
        lightstr = '['
        for l in self.lights:
            if l.get_state():
                lightstr += '#'
            else:
                lightstr += '.'
        lightstr += ']'
        return lightstr
    
    def __eq__(self,s):
        return s == self.__repr__()


if __name__ == '__main__':
    with open('testcase') as f:
        lines = f.readlines()

        indicators = []
        buttons = []
        joltages = [] # I'm sure we'll need these in part 2

        for l in lines:
            ind,rest = l.split('] ')
            indicators.append(ind+']')
            button,joltage = rest.split('{')
            buttons.append(button)
            joltages.append('{'+joltage)

        



    

