
# # Time limit exceet
# class Solution(object):
#     def findDuplicate(self, nums):
#         for i  in range(len(nums)):
#             j = i + 1
#             while j < len(nums):
#                 if nums[i] == nums[j]:
#                     return nums[i]
#                 j += 1
#         return None



class Solution(object):
    def findDuplicate(self, nums):
        hashSet = set()
        for i in nums:
            if i in hashSet:
                return i
            hashSet.add(i)
        return None
           

        


nums = [1,3,4,2,2]
obj = Solution()
print(obj.findDuplicate(nums))