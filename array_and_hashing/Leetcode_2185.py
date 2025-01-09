# 2185. Counting Words With a Given Prefix
class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        res = 0
        for word in words:
            prefix_len = len(pref)
            if len(word) >= prefix_len and word[:prefix_len] == pref:
                res += 1
        return res


words = ["pay", "attention", "practice", "attend"]
pref = "at"

# words = ["leetcode", "win", "loops", "success"]
# pref = "code"
sol = Solution()
print(sol.prefixCount(words, pref))
