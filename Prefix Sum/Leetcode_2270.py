# 2270. Number of Ways to Split Array
class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix_sum = 0
        for index, num in enumerate(nums):
            prefix_sum += num
            nums[index] = prefix_sum

        res = 0
        for num in nums[:-1]:
            if num >= prefix_sum - num:
                res += 1
        return res


nums = [10, 4, -8, 7]
nums = [2, 3, 1, 0]
sol = Solution()
print(sol.waysToSplitArray(nums))
