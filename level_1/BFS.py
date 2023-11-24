from collections import deque
from level_1.FindStartEnd import find_start, find_target
from level_1.ValidNeighbor import get_neighbors

def bfs(grid):
    start = find_start(grid)
    target = find_target(grid)

    queue = deque([(start, [start])])
    visited = set()

    while queue:
        node, path = queue.popleft()
        visited.add(node)

        if node == target:
            return path

        for neighbor in get_neighbors(node, grid):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return []