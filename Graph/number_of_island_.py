from collections import deque


class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0

        len_row = len(grid)
        len_col = len(grid[0])
        visited = set()
        island_count = 0

        def bfs(row, col):
            queue = deque()
            visited.add((row, col))
            queue.append((row, col))

            while queue:
                row_, col_ = queue.popleft()
                for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    row__ = row_ + i
                    col__ = col_ + j
                    if (
                        row__ in range(len_row)
                        and col__ in range(len_col)
                        and (row__, col__) not in visited
                        and grid[row__][col__] == "1"
                    ):
                        queue.append((row__, col__))
                        visited.add((row__, col__))

        for row in range(len_row):
            for col in range(len_col):
                if grid[row][col] == "1" and (row, col) not in visited:
                    island_count += 1
                    bfs(row, col)

        return island_count


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
sol = Solution()
print(sol.numIslands(grid))
