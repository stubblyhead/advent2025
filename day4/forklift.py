def get_adjacent(grid, row, col):
    adjacent = 0
    for r in range(max(0,row-1),min(len(grid)-1,row+1)+1):
        for c in range(max(0,col-1),min(len(grid[row])-1,col+1)+1):
            if r == row and c == col:
                continue
            if grid[r][c] == '@':
                adjacent += 1

    return adjacent

def get_accessible(grid):
    result = {'accessible_count':0, 'accessible_list':[]}
    for row in range(len(grid)):
        for col in range(len(grid[row])):

            if grid[row][col] == '@' and get_adjacent(grid,row,col) < 4:
                result['accessible_count'] += 1
                result['accessible_list'].append((row,col))
    return result

def count_rolls(grid):
    count = 0
    for row in grid:
        for space in row:
            if space == '@':
                count += 1
    return count


if __name__ == '__main__':
    grid = []
    with open('input') as f:
        for r in f.readlines():
            grid.append(list(r.strip()))
    accessible = 0
    roll_count = 0
    accessible = get_accessible(grid)
    print(accessible['accessible_count'])
    
    roll_count = count_rolls(grid)
    original_count = roll_count
    new_count = None
    while roll_count != new_count:
        roll_count = new_count
        accessible = get_accessible(grid)
        for r,c in accessible['accessible_list']:
            grid[r][c] = '.'
        new_count = count_rolls(grid)

    print(original_count - new_count)


        