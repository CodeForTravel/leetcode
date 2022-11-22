class Solution(object):
    def reverseVowels(self, s):
        vowels = ("a","e","i", "o", "u", 'A','E','I','O','U')
        s_list = [i for i in s]
        l = 0
        r = len(s) -1
        while l <= r:
            if s_list[l] in vowels and s_list[r] in vowels:
                s_list[l], s_list[r] = s_list[r], s_list[l]
                l += 1
                r -= 1
            elif s_list[l] in vowels and s_list[r] not in vowels:
                r -= 1
            elif s_list[r] in vowels and s_list[l] not in vowels:
                l += 1
            else:
                l +=1 
                r -= 1
        return "".join(s_list)
                

        
s = "hello"
# s = "leetcode"

obj = Solution()
print(obj.reverseVowels(s))