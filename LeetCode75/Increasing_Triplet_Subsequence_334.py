class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = second = float("inf")
        for i in nums:
            if i <= first:
                first = i
            elif i <= second:
                second = i
            else:
                return True
        return False


nums = [1, 2, 3, 7, 4]
nums = [5, 4, 3, 2, 1]
nums = [2, 4, -2, -3]

ser = Solution()
print(ser.increasingTriplet(nums))
