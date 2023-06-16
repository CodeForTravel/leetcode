

class Solution(object):
    # def isPalindrome(self, s):
    #     new_string = ''.join(
    #         [c.lower() if (c.isalpha() or c.isdigit()) else '' for c in s])
    #     l = 0
    #     r = len(new_string) - 1
    #     while l < r:
    #         if new_string[l] != new_string[r]:
    #             return False
    #         l += 1
    #         r -= 1
    #     return True

    # ========== Another solution =========
    def isPalindrome(self, s):
        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and not (s[l].isalpha() or s[l].isdigit()):
                l += 1
            while l < r and not (s[r].isalpha() or s[r].isdigit()):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


s = "A man, a plan, a canal: Panama"
s = "race a car"
s = " "
obj = Solution()
print(obj.isPalindrome(s))
