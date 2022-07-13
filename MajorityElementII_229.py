class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashMap = {}
        res = []
        for i in nums:
            hashMap[i] = 1 + hashMap.get(i, 0)

            if hashMap[i] > (len(nums)//3):
                if i not in res:
                    res.append(i)
        return res


nums = [2,2,1,1,1,2,2]
nums = [3,2,3]
nums = [1,2]
obj = Solution()
print(obj.majorityElement(nums))