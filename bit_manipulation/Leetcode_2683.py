# 2683. Neighboring Bitwise XOR


class Solution(object):
    def doesValidArrayExist(self, derived):
        """
        :type derived: List[int]
        :rtype: bool
        """
        res = 0
        for i in derived:
            res ^= i
        return True if res == 0 else False


derived = [1, 1, 0]
sol = Solution()
print(sol.doesValidArrayExist(derived))
