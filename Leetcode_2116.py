# 2116. Check if a Parentheses String Can Be Valid
class Solution(object):
    def canBeValid(self, s, locked):
        """
        :type s: str
        :type locked: str
        :rtype: bool
        """
        if len(s) % 2 == 1:
            return False

        locked_stack = []
        unlock_stact = []
        for i in range(len(s)):
            if locked[i] == "0":
                unlock_stact.append(i)
            elif s[i] == "(":
                locked_stack.append(i)
            else:
                if locked_stack:
                    locked_stack.pop()
                elif unlock_stact:
                    unlock_stact.pop()
                else:
                    return False

        while locked_stack and unlock_stact and locked_stack[-1] < unlock_stact[-1]:
            locked_stack.pop()
            unlock_stact.pop()

        if locked_stack:
            return False

        return True


# s = "))()))"
# locked = "010100"

# s = ")"
# locked = "0"

# s = "()()"
# locked = "0000"

s = "()"
locked = "11"
sol = Solution()
print(sol.canBeValid(s, locked))
