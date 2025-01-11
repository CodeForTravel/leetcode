from collections import Counter


class Solution(object):
    def canConstruct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        if len(s) < k:
            return False

        counter = Counter(s)
        unique_counter = 0
        for key, value in counter.items():
            remaining = value % 2
            unique_counter += remaining

        return k >= unique_counter


s = "annabelle"
k = 2

s = "leetcode"
k = 3

s = "true"
k = 4
sol = Solution()
print(sol.canConstruct(s, k))
