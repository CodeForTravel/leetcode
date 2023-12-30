class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        start = 0
        end = 0
        res = 0
        zero_count = 0

        while end < len(nums):
            if nums[end] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[start] == 0:
                    zero_count -= 1
                start += 1
            res = max(res, end - start + 1)
            end += 1
        return res


nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
sol = Solution()
print(sol.longestOnes(nums, k))
