from collections import defaultdict


class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """

        self.graph = self.convert_adjacency_matrix_to_list(isConnected)
        visited = set()
        res = 0
        for key, values in self.graph.items():
            if key not in visited:
                visited.add(key)
                res += 1
                for i in values:
                    self.dfs(i, visited)
        return res

    def dfs(self, node, visited):
        if node not in visited:
            visited.add(node)
            neighbors = self.graph[node]
            for i in neighbors:
                self.dfs(i, visited)

    def convert_adjacency_matrix_to_list(self, list_):
        adjacency_list = defaultdict(list)
        for i in range(len(list_)):
            adjacency_list[i + 1] = []

        # converting adjacency matric to adjacecncy list
        for i in range(len(list_)):
            for j in range(len(list_)):
                if list_[i][j] == 1 and i != j:
                    adjacency_list[i + 1].append(j + 1)
        return adjacency_list


isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
isConnected = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

sol = Solution()
print(sol.findCircleNum(isConnected))
