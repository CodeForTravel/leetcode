class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # return True if len(set(nums)) != len(nums) else False   

        hash_map = set()
        for i in nums:
            if i in hash_map:
                return True
            hash_map.add(i)
        return False
        



nums = [ 2, 3, 1]
# nums = [1, 2, 3, 4]
obj = Solution()
print(obj.containsDuplicate(nums))