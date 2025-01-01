# 3264. Final Array State After K Multiplication Operations I


class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """

        for j in range(k):
            hash_map = {"value": nums[0], "index": 0}
            for i, num in enumerate(nums):
                if hash_map["value"] > num:
                    hash_map["index"] = i
                    hash_map["value"] = num
            nums[hash_map["index"]] = nums[hash_map["index"]] * multiplier
        return nums


nums = [2, 10, 3, 5, 6]
k = 5
multiplier = 2
sol = Solution()
print(sol.getFinalState(nums, k, multiplier))
