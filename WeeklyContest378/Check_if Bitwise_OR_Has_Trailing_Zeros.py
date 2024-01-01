from itertools import combinations


class Solution(object):
    def hasTrailingZeros(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for r in range(2, len(nums) + 1):
            for combo in combinations(nums, r):
                print(combo)
                bitwise_or_result = combo[0]
                for num in combo[1:]:
                    bitwise_or_result |= num

        return False


# TIME LIMIT EXCEED

nums = [1, 3, 5, 7, 9]
sol = Solution()
print(sol.hasTrailingZeros(nums))
