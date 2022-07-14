class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = list(set(nums))
        nums.sort()
        print(nums)
        if len(nums) >= 3:
            return nums[-3]
        return nums[-1]
        


nums = [2,2,3]
nums = [-1,2,3]
obj = Solution()
print(obj.thirdMax(nums))