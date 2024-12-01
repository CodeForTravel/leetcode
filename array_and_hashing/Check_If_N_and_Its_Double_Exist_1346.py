class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] == 2 * arr[j] or arr[i] * 2 == arr[j]:
                    return True
        return False


arr = [10, 2, 5, 3]
arr = [7, 1, 14, 11]

sol = Solution()
print(sol.checkIfExist(arr))


# print(i, j)
# print(arr[i], 2 * arr[j])
# print("====================")
