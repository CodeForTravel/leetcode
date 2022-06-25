class Solution(object):
    def missingNumber(self, nums):
        for i in range(len(nums)+1):
            if i not in nums:
                return i
        
nums = [3,0,1]
nums = [9,6,4,2,3,5,7,0,1]
obj = Solution()
print(obj.missingNumber(nums))