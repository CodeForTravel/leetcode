
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = nums[0]
        current_sum = 0
        for num in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += num

            if current_sum > result:
                result = current_sum
        return result


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]  # s = "()[]{}"
obj = Solution()
print(obj.maxSubArray(nums))
