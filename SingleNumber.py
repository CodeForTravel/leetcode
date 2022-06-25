
class Solution(object):
    def singleNumber(self, nums):
        hashSet = set()
        for i in nums:
            if i in hashSet:
                hashSet.remove(i)
            else:
                hashSet.add(i)
        return hashSet.pop()
           

        


nums = [4,1,2,1,2]
obj = Solution()
print(obj.singleNumber(nums))