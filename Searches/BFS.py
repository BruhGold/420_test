from collections import deque
from Searches.FindStartEnd import find_start, find_target
from Searches.ValidNeighbor import get_neighbors

def bfs(grid):
    start = find_start(grid)
    target = find_target(grid)

    queue = deque([(start, [start], set())])
    visited = set()

    while queue:
        node, path, keys = queue.popleft()
        visited.add(node)

        if node == target:
            return path

        for neighbor in get_neighbors(node, grid, keys):
            if neighbor not in visited:
                new_keys = keys.copy()
                if grid[neighbor[0]][neighbor[1]] and grid[neighbor[0]][neighbor[1]][0] == 'K':
                    new_keys.add(grid[neighbor[0]][neighbor[1]])
                queue.append((neighbor, path + [neighbor], new_keys))

    return []