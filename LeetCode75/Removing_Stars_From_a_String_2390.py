class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        my_stack = []
        for ch in s:
            if ch == "*":
                my_stack.pop()
            else:
                my_stack.append(ch)
        return "".join(my_stack)


s = "leet**cod*e"
sol = Solution()
print(sol.removeStars(s))
