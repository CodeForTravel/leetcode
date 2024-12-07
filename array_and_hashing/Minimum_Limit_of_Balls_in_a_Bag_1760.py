class Solution(object):
    def minimumSize(self, nums, maxOperations):
        def canDivide(maxBagSize):
            # Calculate the total operations needed for maxBagSize
            operations = 0
            for balls in nums:
                operations += (balls - 1) // maxBagSize  # Equivalent to ceil(balls / maxBagSize) - 1
            return operations <= maxOperations

        # Binary search for the minimum maxBagSize
        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if canDivide(mid):
                right = mid  # Try for a smaller maxBagSize
            else:
                left = mid + 1  # Increase maxBagSize
        return left


nums = [9]
maxOperations = 2
sol = Solution()
print(sol.minimumSize(nums, maxOperations))
# Need to clear more
