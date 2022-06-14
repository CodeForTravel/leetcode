class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # this is one solution
        # return False if len(set(nums)) == len(nums) else True

        # another solution
        num_set = set()
        for i in nums:
            if i in num_set:
                return True
            num_set.add(i)
        return False


nums = [1, 2, 3, 1]
# nums = [1, 2, 3, 4]
obj = Solution()
print(obj.containsDuplicate(nums))
