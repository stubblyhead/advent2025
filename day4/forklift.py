def get_adjacent(grid, row, col):
    adjacent = 0
    for r in range(max(0,row-1),min(len(grid),row+1)):
        for c in range(max(0,col-1),min(len(grid[row]),col+1)):
            if grid[r][c] == '@':
                adjacent += 1

    return adjacent


if __name__ == '__main__':
    with open('testcase') as f:
        grid = list(map(str.strip, f.readlines()))
    accessible = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '.' and get_adjacent(grid,row,col) < 4:
                accessible += 1
    print(accessible)

        