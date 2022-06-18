class Solution(object):
    def removeDuplicates(self, nums):
        # if len(nums) <= 1:
        #     return len(nums)

        # l = 0
        # r = l+1
        # while r < len(nums):
        #     if nums[l] == nums[r]:
        #         del nums[r]
        #         l = 0
        #         r = l+1
        #     elif nums[l] != nums[r]:
        #         l = r 
        #         r = l + 1
        # return len(nums)

        # a better solution

        length = 0
        if len(nums) == 0: return length
        for i in range(1,len(nums)):
            if nums[length] < nums[i]:
                length += 1
                nums[length] = nums[i]
        return length+1


nums = [0,0,1,1,1,2,2,3,3,4]
# nums = [0]
obj = Solution()
print(obj.removeDuplicates(nums))