class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = 0
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.remove(val)
                i = length
            else:
                i += 1
                length = i
        return len(nums)
                
            



nums = [0,0,1,1,1,2,2,3,3,4]
val = 1
# nums = [0]
obj = Solution()
print(obj.removeElement(nums, val))