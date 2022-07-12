class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashMap = {}
        for i in nums:
            hashMap[i] = 1 + hashMap.get(i, 0)

            if hashMap[i] > (len(nums)//2):
                return i

    # # another solution
    # def majorityElement(self, nums):
    #     return sorted(nums)[len(nums)//2]

nums = [2,2,1,1,1,2,2]
obj = Solution()
print(obj.majorityElement(nums))