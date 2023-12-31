class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        consecutive_one_count = 0
        for n in nums:
            if n == 1:
                consecutive_one_count += 1
                if consecutive_one_count > res:
                    res = consecutive_one_count
            if n == 0:
                consecutive_one_count = 0
        return res


nums = [1, 1, 0, 1, 1, 1]
# nums = [1, 0, 1, 1, 0, 1]
# nums = [1, 1, 0, 1]
# Output: 3
obj = Solution()
print(obj.findMaxConsecutiveOnes(nums))
