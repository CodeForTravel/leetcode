class Solution(object):
    def lengthOfLongestSubstring(self, s):
        charSet = set()
        max_length = 0
        l,r = 0,0
        while r < len(s):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            max_length = max(max_length, r-l+1)
            r += 1
        return max_length



s = "bbbbb"
s = "abcabcbb"
s = "pwwkew"
obj = Solution()
print(obj.lengthOfLongestSubstring(s))