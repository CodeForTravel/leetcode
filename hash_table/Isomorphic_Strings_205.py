class Solution(object):
    def isIsomorphic(self, s, t):
        dcit1, dict2 = dict(), dict()
        for v, w in zip(s,t):
            if (v in dcit1 and dcit1[v] != w) or (w in dict2 and dict2[w] != v):
                    return False
            dcit1[v], dict2[w] = w, v
        return True
        
# s = "egg"
# t = "add"
s = "paper"
t = "title"

obj = Solution()
print(obj.isIsomorphic(s, t))