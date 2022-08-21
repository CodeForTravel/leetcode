
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        hash_map = {}
        for i, v in enumerate(nums):
            if v in hash_map and abs(hash_map.get(v) - i) <= k:
                return True
            else:
                hash_map[v] = i
        return False
        
        
# nums = [1,2,3,1]
# k = 3
# nums = [1,0,1,1]
# k = 1
nums = [1,2,3,1,2,3]
k = 2
obj = Solution()
print(obj.containsNearbyDuplicate(nums, k))