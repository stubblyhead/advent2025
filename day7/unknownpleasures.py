class GridSpace:
    def __init__(self):
        pass

class Reflector(GridSpace):
    def __init__(self):
        self.activated = False

    def activate(self):
        self.activated = True

    def get_activation_status(self):
        return self.activated
    
class EmptySpace(GridSpace):
    def __init__(self):
        self.has_beam = False
        self.beam_count = 0

    def energize(self, in_beams):
        self.has_beam = True
        self.beam_count += in_beams

    def get_beam_status(self):
        return self.has_beam
    
    def get_beam_count(self):
        return self.beam_count

if __name__ == '__main__':
    with open('input') as f:
        lines = f.readlines()

    grid = []
    for l in map(str.strip, lines):
        this_line = []
        for space in l:
            if space in ['.','S']:
                this_line.append(EmptySpace())
                if space == 'S':
                    this_line[-1].energize(1)

            elif space == '^':
                this_line.append(Reflector())
        grid.append(this_line)


    for r in range(len(grid)-1):
        for c in range(len(grid[r])):
            if type(grid[r][c]) == EmptySpace and grid[r][c].get_beam_status():
                if type(grid[r+1][c]) == EmptySpace:
                    grid[r+1][c].energize(grid[r][c].get_beam_count())
                else:
                    grid[r+1][c].activate()
                    grid[r+1][c-1].energize(grid[r][c].get_beam_count())
                    grid[r+1][c+1].energize(grid[r][c].get_beam_count())

    active_count = 0
    for row in grid:
        for space in row:
            if type(space) == Reflector and space.get_activation_status():
                active_count += 1
    print(active_count)
    total_beams = 0
    for space in grid[-1]:
        total_beams += space.beam_count

    print(total_beams)