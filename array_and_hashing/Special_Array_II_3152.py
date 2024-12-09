# class Solution(object):
#     def isArraySpecial(self, nums, queries):
#         for i, query in enumerate(queries):
#             queries[i] = self.helper_function(query, nums)
#         return queries

#     def helper_function(self, query, nums):
#         start, end = query[0], query[-1] + 1
#         previous = nums[start] % 2
#         for i in range(start + 1, end):
#             current = nums[i] % 2
#             if current == previous:
#                 return False
#             previous = current
#         return True


class Solution(object):
    def isArraySpecial(self, nums, queries):
        previous = nums[0] % 2
        nums[0] = 1
        count = 1
        for i in range(1, len(nums)):
            current = nums[i] % 2
            if current != previous:
                count += 1
                nums[i] = count
            else:
                count = 1
                nums[i] = count
            previous = current

        for i, query in enumerate(queries):
            left, right = query[0], query[1]
            queries[i] = nums[right] >= right - left + 1
        return queries


nums = [3, 4, 1, 2, 6]
queries = [[0, 4]]

# nums = [4, 5, 8, 3, 1, 6]
# nums = [4, 3, 1, 6]
# queries = [[0, 2], [2, 3]]

sol = Solution()
print(sol.isArraySpecial(nums, queries))
