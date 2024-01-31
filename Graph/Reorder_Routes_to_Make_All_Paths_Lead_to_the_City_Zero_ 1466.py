from collections import defaultdict


class Solution(object):
    def minReorder(self, n, connections):
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append((v, 1))  # 1 represents the direction from u to v
            graph[v].append((u, 0))  # 0 represents the direction from v to u

        visited = set()
        result = 0

        def dfs(node):
            nonlocal result
            visited.add(node)

            for neighbor, direction in graph[node]:
                if neighbor not in visited:
                    result += direction
                    dfs(neighbor)

        dfs(0)
        return result


# Example usage:
n = 6
connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
results = [0, 1, 1, 1, 1]

# Create an instance of the Solution class
solution_instance = Solution()

# Call the method using the instance
print(solution_instance.minReorder(n, connections))


data = {
    0: [(1, 1), (4, 0)],
    1: [(0, 0), (3, 1)],
    3: [(1, 0), (2, 0)],
    2: [(3, 1)],
    4: [(0, 1), (5, 1)],
    5: [(4, 0)],
}
