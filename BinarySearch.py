class Solution(object):
    def search(self, nums, target):
        low, high = 0, len(nums)-1
        def binary_search(nums, low, high, target):
            if high >= low:
                mid = (high+low) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    return binary_search(nums, low, mid-1, target)
                else:
                    return binary_search(nums, mid+1, high, target)
            return -1
        target_position = binary_search(nums, low, high, target)
        return target_position
        

nums = [-1,0,3,5,9,12]
target = 9
obj = Solution()
print(obj.search(nums, target))