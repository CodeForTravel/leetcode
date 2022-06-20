class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashDict = {}
        for i in nums:
            hashDict[i] = hashDict.get(i, 0) + 1
        
        for value in hashDict.values():
            if value > 1:
                return True
                break
        return False
        


nums = [1,2,3,1]
nums = [1,2,3,4]
nums = [1,1,1,3,3,4,3,2,4,2]
obj = Solution()
print(obj.containsDuplicate(nums))