class Solution(object):
    def isValid(self, s):
        stack = []
        closeToOpen = {")": "(", "}": "{", "]": "["}

        for ch in s:
            print(ch)
            if ch in closeToOpen:
                import pdb

                pdb.set_trace()
                if stack and stack[-1] == closeToOpen[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return True if not stack else False


s = "((){]})[]{}"

obj = Solution()
print(obj.isValid(s))
