def find_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'A':
                print(f"Start: {i, j}")
                return (i, j)

def find_target(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'T':
                print(f"Target: {i, j}")
                return (i, j)