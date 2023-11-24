from Searches.FindStartEnd import find_start, find_target
from Searches.ValidNeighbor import get_neighbors

def dfs(grid):
    def dfs_helper(node, target, keys):
        visited.add(node)
        path.append(node)

        if node == target:
            return True

        for neighbor in get_neighbors(node, grid, keys):
            if neighbor not in visited:
                if grid[neighbor[0]][neighbor[1]] and grid[neighbor[0]][neighbor[1]][0] == 'K':
                    keys.append(grid[neighbor[0]][neighbor[1]])
                if dfs_helper(neighbor, target, keys):
                    return True

        # If the target is not found, remove the keys collected during the current path
        if path[-1] == node:  # To avoid removing keys multiple times
            path.pop()
            while len(keys) > 0 and keys[-1] in path:  # Remove keys collected on the current path
                keys.pop()

        return False

    visited = set()
    path = []

    start = find_start(grid)
    target = find_target(grid)
    keys = []

    dfs_helper(start, target, keys)
    return path
