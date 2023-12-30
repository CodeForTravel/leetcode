# class Solution(object):
#     def findMaxAverage(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: float
#         """

#         max_sum = sum(nums[:k])
#         max_sum = float(max_sum)

#         start_index = 0
#         end_index = k
#         while end_index < len(nums):
#             sum_ = max_sum - nums[start_index]
#             start_index += 1

#             sum_ = sum_ + nums[end_index]
#             end_index += 1

#             max_sum = max(sum_, max_sum)
#         return max_sum / k


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        max_sum = window = float(sum(nums[:k]))
        for i in range(1, len(nums) - k + 1):
            window = window - nums[i - 1] + nums[i + k - 1]
            max_sum = max(window, max_sum)
        return max_sum / k


nums = [1, 12, -5, -6, 50, 3]
k = 4
nums = [0, 4, 0, 3, 2]
k = 1
ser = Solution()
print(ser.findMaxAverage(nums, k))
