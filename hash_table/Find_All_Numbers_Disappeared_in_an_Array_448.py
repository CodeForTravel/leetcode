class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # hash_dict = {}
        # for i in nums:
        #     hash_dict[i] = i
        hash_map = set(nums)
        res = []
        for j in range(1, len(nums)+1):
            if j not in hash_map:
                res.append(j)
        return res

        

            
        

nums = [4,3,2,7,8,2,3,1]
# nums = [1,1]
obj = Solution()
print(obj.findDisappearedNumbers(nums))