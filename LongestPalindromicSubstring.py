
# traditional  way
# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         length = len(s)
#         if length == 1:
#             return s
#         longest_seq = 0
#         results = {}
#         for i, char in enumerate(s):
#             for j, char in enumerate(s):
#                 if s[i:j+1] and self.is_palindrom(s[i:j+1]):
#                     results[len(s[i:j+1])] = s[i:j+1]
#         return results[max(results)]

#     def is_palindrom(self, s):
#         return s[::-1] == s


# s = "bb"
# obj = Solution()
# print(obj.longestPalindrome(s))


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        resultLength = 0

        for i in range(len(s)):

            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > resultLength:
                    resultLength = r-l+1
                    result = s[l:r+1]
                l -= 1
                r += 1

            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > resultLength:
                    resultLength = r-l+1
                    result = s[l:r+1]
                l -= 1
                r += 1

        return result


s = "cbbd"
obj = Solution()
print(obj.longestPalindrome(s))
