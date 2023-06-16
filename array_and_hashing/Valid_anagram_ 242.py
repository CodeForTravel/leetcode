
# =============  solution 1 ===============
# class Solution(object):
#     def isAnagram(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """
#         s_hash = dict()
#         t_hash = dict()
        
#         for i in s:
#             s_hash[i] = 1 + s_hash.get(i, 0)
        
#         for j in t:
#             t_hash[j] = 1 + t_hash.get(j, 0)
#         return s_hash == t_hash


# =============  solution 2 ===============
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        s_count_hash = dict()
        t_count_hash = dict()

        for i in range(len(s)):
            s_count_hash[s[i]] = 1 + s_count_hash.get(s[i], 0)
            t_count_hash[t[i]] = 1 + t_count_hash.get(t[i], 0)

        return s_count_hash == t_count_hash


s = "anagram"
t = "nagaram"
s = "rat"
t = "car"
obj = Solution()
print(obj.isAnagram(s,t))