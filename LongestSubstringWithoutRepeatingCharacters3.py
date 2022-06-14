
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         result_length = 0

#         for i in range(len(s)):

#             l, r = i, i
#             while l >= 0 and r < len(s):
#                 new_string = s[l:r+1]
#                 set_sting = set(s[l:r+1])
#                 if len(new_string) != len(set_sting):
#                     break
#                 elif result_length < len(new_string):
#                     result_length = len(new_string)
#                 l -= 1
#                 r += 1

#             l, r = i, i+1
#             while l >= 0 and r < len(s):
#                 new_string = s[l:r+1]
#                 set_sting = set(s[l:r+1])
#                 if len(new_string) != len(set_sting):
#                     break
#                 elif result_length < len(new_string):
#                     result_length = len(new_string)
#                 l -= 1
#                 r += 1

#         return result_length


# optimal solution
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charSet = set()
        result_length = 0
        l = 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            result_length = max(result_length, r-l+1)
        return result_length


s = "dvdf"
obj = Solution()
print(obj.lengthOfLongestSubstring(s))
