from collections import defaultdict


# class Solution(object):
#     def maximumLength(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         max_count = -1
#         count_dict = defaultdict(set())
#         for i in s:
#             count_dict[i] = count_dict.get(i, 0) + 1
#             max_count = max(max_count, count_dict.get(i))

#         if max_count < 3:
#             return -1
#         else:
#             return max_count - 2


class Solution(object):
    def maximumLength(self, s):
        n = len(s)
        substring_count = {}

        # Generate all possible substrings
        for i in range(n):
            for j in range(i + 1, n + 1):
                substring = s[i:j]
                if substring not in substring_count:
                    substring_count[substring] = 0
                substring_count[substring] += 1

        # Find the longest substring that occurs exactly three times
        longest_substring = ""
        for substring, count in substring_count.items():
            if count == 3 and len(substring) > len(longest_substring):
                longest_substring = substring
        return longest_substring


# s = "aaaa"
s = "abcdef"
s = "abcaba"
sol = Solution()
print(sol.maximumLength(s))
