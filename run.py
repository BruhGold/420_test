# run.py

from Searches.DFS import dfs
from Searches.BFS import bfs

def main():
    # Example grid (replace this with your actual data)
    grid = [
        ['-1', '0', '0', '0', '0'],
        ['A', '-1', '0', 'K1', '0'],
        ['0', '0', '0', '0','0'],
        ['0', 'K2', '0', 'D1', 'D2'],
        ['0', '0', '0', '-1', 'T']
    ]

    # Perform DFS
    print("DFS:")
    dfs_path = dfs(grid)
    print(dfs_path)

    # Perform BFS
    print("\nBFS:")
    bfs_path = bfs(grid)
    print(bfs_path)

if __name__ == "__main__":
    main()

