# from collections import defaultdict


# class Solution(object):
#     def maxOperations(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         hash_map = defaultdict(int)
#         res = 0

#         for i in nums:
#             if i >= k:
#                 continue

#             dif = k - i
#             if hash_map[dif] > 0:
#                 res += 1
#                 hash_map[dif] -= 1
#             else:
#                 hash_map[i] += 1

#         return res


# ============================= This solution beat over 95% solution ===========================
# python3


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        res, l, r = 0, 0, len(nums) - 1

        while l < r:
            S = nums[l] + nums[r]
            if S > k:
                r -= 1
            elif S < k:
                l += 1
            else:
                res += 1
                l += 1
                r -= 1
        return res


# nums = [3, 1, 3, 4, 3]
# k = 6
# nums = [1, 2, 3, 4]
# k = 5
nums = [2, 5, 4, 4, 1, 3, 4, 4, 1, 4, 4, 1, 2, 1, 2, 2, 3, 2, 4, 2]
k = 3
sol = Solution()
print(sol.maxOperations(nums, k))
