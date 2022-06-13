class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i, char in enumerate(s):
            sub_string = s[:i]
            print(sub_string)
        return ""


s = "abcabcbb"
obj = Solution()
print(obj.lengthOfLongestSubstring(s))
