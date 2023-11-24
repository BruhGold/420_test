def get_neighbors(node, grid):
    i, j = node
    neighbors = []

    def is_valid(x, y):
        return (
            0 <= x < len(grid)
            and 0 <= y < len(grid[0])
            and grid[x][y] != '-1'
        )

    # Check upper neighbor
    if is_valid(i - 1, j):
        neighbors.append((i - 1, j))

    # Check lower neighbor
    if is_valid(i + 1, j):
        neighbors.append((i + 1, j))

    # Check left neighbor
    if is_valid(i, j - 1):
        neighbors.append((i, j - 1))

    # Check right neighbor
    if is_valid(i, j + 1):
        neighbors.append((i, j + 1))

    # Check upper-left neighbor (diagonal)
    if is_valid(i - 1, j - 1) and (is_valid(i - 1, j) or is_valid(i, j - 1)):
        neighbors.append((i - 1, j - 1))

    # Check upper-right neighbor (diagonal)
    if is_valid(i - 1, j + 1) and (is_valid(i - 1, j) or is_valid(i, j + 1)):
        neighbors.append((i - 1, j + 1))

    # Check lower-left neighbor (diagonal)
    if is_valid(i + 1, j - 1) and (is_valid(i + 1, j) or is_valid(i, j - 1)):
        neighbors.append((i + 1, j - 1))

    # Check lower-right neighbor (diagonal)
    if is_valid(i + 1, j + 1) and (is_valid(i + 1, j) or is_valid(i, j + 1)):
        neighbors.append((i + 1, j + 1))

    return neighbors
