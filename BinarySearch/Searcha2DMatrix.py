# class Solution(object):
#     def searchMatrix(self, matrix, target):
#         new_list = []
#         for li in matrix:
#             new_list.extend(li)
        
#         low, high = 0, len(new_list)-1
#         def binary_search(new_list, low, high, target):
#             if high >= low:
#                 mid = (high+low) // 2
#                 if new_list[mid] == target:
#                     return True
#                 elif new_list[mid] > target:
#                     return binary_search(new_list, low, mid-1, target)
#                 else:
#                     return binary_search(new_list, mid+1, high, target)
#             return False
#         target_position = binary_search(new_list, low, high, target)
#         return target_position



class Solution:
    def searchMatrix(self, matrix, target):
        ROWS, COLS = len(matrix), len(matrix[0])
        
        top, bot = 0, ROWS - 1
        while top <= bot:
            midRow = (top + bot) // 2
            if target > matrix[midRow][-1]:
                top = midRow + 1
            elif target < matrix[midRow][0]:
                bot = midRow - 1
            else:
                break
        
        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
        
        

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# target = 13

obj = Solution()
print(obj.searchMatrix(matrix, target))