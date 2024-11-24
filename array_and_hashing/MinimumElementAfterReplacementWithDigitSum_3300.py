class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_value = float("+inf")
        for num in nums:
            min_value = min(min_value, self.digit_sum_helper(num))
        return min_value

    def digit_sum_helper(self, number):
        total = 0
        while number > 0:
            total += number % 10
            number //= 10
        return total


# nums = [10, 12, 13, 14]
nums = [999, 19, 199]
sol = Solution()
print(sol.minElement(nums))
