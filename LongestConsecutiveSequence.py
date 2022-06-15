class Solution(object):
    def longestConsecutive(self, nums):
        numSet = set(nums)
        result = 0
        for num in nums:
            if num-1 not in numSet:
                length = 0
                while num + length in numSet:
                    length += 1
                result = max(length, result)
        return result


# nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
nums = [100, 4, 200, 1, 3, 2]
nums = [0, 0]
obj = Solution()
print(obj.longestConsecutive(nums))
