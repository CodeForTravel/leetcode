from collections import Counter


class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        s_counter = Counter(s)
        for i in s_counter.values():
            if i <= 2:
                res += i
            elif i % 2 == 1:
                res += 1
            else:
                res += 2
        return res


s = "abaacbcbb"
# s = "aa"
sol = Solution()
print(sol.minimumLength(s))
