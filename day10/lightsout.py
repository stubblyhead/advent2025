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

    def set_lights(self,pattern):
        pattern = pattern[1:-1]
        for l in range(len(pattern)):
            if pattern[l] == '#':
                self.lights[l].turn_on()
            else:
                self.lights[l].turn_off()


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
    
    def __ne__(self,s):
        return not self == s


if __name__ == '__main__':
    with open('input') as f:
        lines = f.readlines()

    targets = []
    light_arrays = []
    buttons = []
    joltages = [] # I'm sure we'll need these in part 2

    for l in lines:
        ind,rest = l.split('] ')
        targets.append(ind+']')
        light_arrays.append(LightArray(len(targets[-1])-2))
        button,joltage = rest.split('{')
        buttons.append(button)
        joltages.append('{'+joltage.strip())
    total_presses = 0
    memo = {} # keeping this in my back pocket

    for line in range(len(lines)):
        t = targets[line]
        la = light_arrays[line]
        b = buttons[line].split()
        presses = 0
        found = False
        while not found:
            presses += 1
            for comb in cwr([i for i in range(len(b))], r=presses):
                la.reset()
                for press in comb:
                    la.press_button(b[press])
                if la == t:
                    found = True
                    break
                else:
                    memo[comb] = la.__repr__()
        total_presses += presses

    print(total_presses)

    

