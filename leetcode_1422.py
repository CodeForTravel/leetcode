# 1422. Maximum Score After Splitting a String


# class Solution(object):
#     def maxScore(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """

#         if len(s) < 3:
#             count = 0
#             if s[0] == "0":
#                 count += 1
#             if s[1] == "1":
#                 count += 1
#             return count

#         left_prefix = [0] * len(s)
#         right_prefix = [0] * len(s)
#         for index, ch in enumerate(s):
#             if ch == "0":
#                 left_prefix[index] = 1 + left_prefix[index - 1]
#             else:
#                 left_prefix[index] = left_prefix[index - 1]

#         for index, ch in enumerate(reversed(s)):
#             if ch == "1":
#                 right_prefix[index] = 1 + right_prefix[index - 1]
#             else:
#                 right_prefix[index] = right_prefix[index - 1]

#         right_prefix.reverse()
#         res = 0
#         for i in range(1, len(s) - 1):
#             res = max(left_prefix[i] + right_prefix[i], res)
#         return res


class Solution:
    def maxScore(self, s: str) -> int:
        left_count = 0  # count of "0"s on the left side
        right_count = s.count("1")  # total count of "1"s in the entire string

        max_score = 0

        # Iterate over each possible split point (between characters)
        for i in range(len(s) - 1):  # no split at the end (len(s) - 1)
            if s[i] == "0":
                left_count += 1
            elif s[i] == "1":
                right_count -= 1

            # Calculate the current score for this split
            max_score = max(max_score, left_count + right_count)

        return max_score


s = "1111"
s = "00"
sol = Solution()
print(sol.maxScore(s))
