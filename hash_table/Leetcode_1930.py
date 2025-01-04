# 1930. Unique Length-3 Palindromic Subsequences

# class Solution(object):
#     def countPalindromicSubsequence(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         res = 0
#         hash_map = {}

#         for i in range(len(s)):
#             if hash_map.get(s[i]):
#                 hash_map[s[i]][1] = i
#             else:
#                 hash_map[s[i]] = [i, i]

#         for value in hash_map.values():
#             start = value[0]
#             end = value[1]
#             if start == end:
#                 continue
#             res += len(set(s[start + 1 : end]))
#         return res


# More optimal solution
# ==============
class Solution(object):
    def countPalindromicSubsequence(self, s):
        res = 0
        uniq = set(s)
        for c in uniq:
            start = s.find(c)
            end = s.rfind(c)
            if start < end:
                d = set(s[start + 1 : end])
                res += len(d)

        return res


s = "aabca"
# s = "adc"
sol = Solution()
print(sol.countPalindromicSubsequence(s))
