

class Solution(object):
    def isPalindrome(self, s):
        new_string = ''.join(
            [c.lower() if (c.isalpha() or c.isdigit()) else '' for c in s])
        l = 0
        r = len(new_string) - 1
        while l < r:
            if new_string[l] != new_string[r]:
                return False
            l += 1
            r -= 1
        return True


s = "A man, a plan, a canal: Panama"
obj = Solution()
print(obj.isPalindrome(s))
