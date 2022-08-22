
class Solution(object):
    def wordPattern(self, pattern, s):
        hash_map1, hash_map2 = {}, {}
        s_list = s.split()
        if len(pattern) != len(s_list):
            return False
        
        for p, w in zip(pattern, s_list):
            if (p in hash_map1 and hash_map1[p] != w) or (w in hash_map2 and hash_map2[w] != p):
                return False
            hash_map1[p] = w
            hash_map2[w] = p
        return True
        

pattern = "abba"
s = "dog cat cat dog"

# pattern = "abba"
# s = "dog cat cat dog"
# pattern = "abba"
# s = "dog cat cat fish"
obj = Solution()
print(obj.wordPattern(pattern, s))