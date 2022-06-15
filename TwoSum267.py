
class Solution(object):
    def twoSum(self, numbers, target):
        l = 0
        r = len(numbers) - 1
        while l < r:
            current_sum = numbers[l] + numbers[r]
            if current_sum > target:
                r -= 1
            elif current_sum < target:
                l += 1
            else:
                return [l+1, r+1]
        return []


# numbers = [2, 7, 11, 15]
# target = 9
# numbers = [-1, 0]
# target = -1
numbers = [1, 2, 3, 4, 5, 7, 10, 11]
target = 9
obj = Solution()
print(obj.twoSum(numbers, target))
