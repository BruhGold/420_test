from level_1.FindStartEnd import find_start, find_target
from level_1.ValidNeighbor import get_neighbors

def dfs(grid):
    def dfs_helper(node, target):
        visited.add(node)
        path.append(node)

        if node == target:
            return True

        for neighbor in get_neighbors(node, grid):
            if neighbor not in visited:
                if dfs_helper(neighbor, target):
                    return True

        # If the target is not found backtrack
        if path[-1] == node:  
            path.pop()

        return False

    visited = set()
    path = []

    start = find_start(grid)
    target = find_target(grid)

    dfs_helper(start, target)
    return path
