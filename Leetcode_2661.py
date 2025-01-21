# class Solution(object):
## TIme Limit Exceed
#     def firstCompleteIndex(self, arr, mat):
#         """
#         :type arr: List[int]
#         :type mat: List[List[int]]
#         :rtype: int
#         """

#         rows, cols = len(mat), len(mat[0])
#         mat_set = [set(m) for m in mat]

#         for i in range(cols):
#             temp_set = set()
#             for j in range(rows):
#                 temp_set.add(mat[j][i])
#             mat_set.append(temp_set)

#         for index, num in enumerate(arr):
#             for i in range(len(mat_set)):
#                 if num in mat_set[i]:
#                     mat_set[i].remove(num)
#                 if not mat_set[i]:
#                     return index


class Solution(object):
    def firstCompleteIndex(self, arr, mat):
        row_counter = {}
        col_counter = {}
        rows, cols = len(mat), len(mat[0])
        hash_map = {}
        for i in range(rows):
            for j in range(cols):
                hash_map[mat[i][j]] = (i, j)

        for index, num in enumerate(arr):
            row, col = hash_map.get(num)

            row_counter[row] = row_counter.get(row, 0) + 1
            col_counter[col] = col_counter.get(col, 0) + 1
            if row_counter[row] == cols or col_counter[col] == rows:
                return index


arr = [1, 3, 4, 2]
mat = [[1, 4], [2, 3]]

arr = [2, 8, 7, 4, 1, 3, 5, 6, 9]
mat = [[3, 2, 5], [1, 4, 6], [8, 7, 9]]

arr = [1, 4, 5, 2, 6, 3]
mat = [[4, 3, 5], [1, 2, 6]]

arr = [6, 2, 3, 1, 4, 5]
mat = [[5, 1], [2, 4], [6, 3]]


sol = Solution()
print(sol.firstCompleteIndex(arr, mat))
