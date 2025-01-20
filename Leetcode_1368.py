from collections import deque


class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up
        dist = [[float("inf")] * n for _ in range(m)]
        dist[0][0] = 0
        deque_ = deque([(0, 0, 0)])  # (cost, x, y)

        while deque_:
            cost, x, y = deque_.popleft()

            # Skip if we already found a shorter path
            if cost > dist[x][y]:
                continue

            for i, (dx, dy) in enumerate(directions):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    # Determine the cost
                    new_cost = cost + (1 if grid[x][y] != i + 1 else 0)

                    # Update and add to the deque
                    if new_cost < dist[nx][ny]:
                        dist[nx][ny] = new_cost
                        if grid[x][y] == i + 1:
                            deque_.appendleft((new_cost, nx, ny))  # Add to the front
                        else:
                            deque_.append((new_cost, nx, ny))  # Add to the back

        return dist[m - 1][n - 1]


grid = [[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]
sol = Solution()
print(sol.minCost(grid))
