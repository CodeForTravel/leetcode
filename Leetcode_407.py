from heapq import heappop, heappush


class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        rows, cols = len(heightMap), len(heightMap[0])
        if rows < 3 or cols < 3:
            return 0
        min_heap = []
        for r in range(rows):
            for c in range(cols):
                if r in [0, rows - 1] or c in [0, cols - 1]:
                    heappush(min_heap, (heightMap[r][c], r, c))
                    heightMap[r][c] = -1
        res = 0
        max_h = -1
        while min_heap:
            h, r, c = heappop(min_heap)
            max_h = max(max_h, h)
            res += max_h - h

            neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
            for nr, nc in neighbors:
                if nr < 0 or nc < 0 or nr == rows or nc == cols or heightMap[nr][nc] == -1:
                    continue
                heappush(min_heap, (heightMap[nr][nc], nr, nc))
                heightMap[nr][nc] = -1

        return res


heightMap = [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]
sol = Solution()
print(sol.trapRainWater(heightMap))
