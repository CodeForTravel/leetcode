class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        # char:index hashmap
        char_index = {}
        res = -1
        for i, ch in enumerate(s):
            if ch in char_index:
                res = max(res, i - char_index[ch] - 1)
            else:
                char_index[ch] = i
        return res


s = "aa"
obj = Solution()
print(obj.maxLengthBetweenEqualCharacters(s))
