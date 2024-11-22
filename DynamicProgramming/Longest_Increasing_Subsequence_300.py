class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        LIS = [1] * length

        for i in range(1, length):
            for j in range(i):
                if nums[i] > nums[j]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)

        return max(LIS)


nums = [10, 9, 2, 5, 3, 7, 101, 18]
sol = Solution()
print(sol.lengthOfLIS(nums))
