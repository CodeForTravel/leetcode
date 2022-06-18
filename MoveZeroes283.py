class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zero = 0  # records the position of "0"
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
        return nums
        

nums = [0,0,1,1,1,2,2,3,3,4]
nums = [0,0,0,0,0,0,1,1,1]

obj = Solution()
print(obj.moveZeroes(nums))