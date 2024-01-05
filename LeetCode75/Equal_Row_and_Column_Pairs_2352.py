from collections import defaultdict


class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        hash_dict = defaultdict(int)
        count = 0
        for row in grid:
            hash_dict[tuple(row)] += 1

        for col in zip(*grid):
            count += hash_dict[tuple(col)]
        return count


grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
sol = Solution()
print(sol.equalPairs(grid))
