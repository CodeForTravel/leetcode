class Solution(object):
    def isAnagram(self, s, t):
        # Solution one
        # s = sorted(s)
        # t = sorted(t)
        # return True if s == t else False

        # =================
        # another solution
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        print(countS)
        print(countT)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True


s = "anagram"
t = "nagaram"
s = "rat"
t = "car"
obj = Solution()
print(obj.isAnagram(s, t))
