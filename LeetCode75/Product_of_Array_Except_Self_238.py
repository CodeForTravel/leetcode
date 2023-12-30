class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = 1
        res = [i for i in nums]
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        prefix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= prefix
            prefix *= nums[i]
        return res


nums = [1, 2, 3, 4]
ser = Solution()
print(ser.productExceptSelf(nums))
