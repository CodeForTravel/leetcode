class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        start = 0
        end = 0
        res = 0
        zero_count = 0

        while end < len(nums):
            if nums[end] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[start] == 0:
                    zero_count -= 1
                start += 1
            res = max(res, end - start)
            end += 1
        return res


nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
nums = [1, 1, 0, 1]
nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
sol = Solution()
print(sol.longestSubarray(nums))
