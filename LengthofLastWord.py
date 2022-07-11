class Solution(object):
    # # with built-in library funtion ==========================
    # def lengthOfLastWord(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
        
    #     s = s.strip()
    #     last_word = s.split(" ")[-1]
    #     return len(last_word)

    # without built-in library funtion ===========================
    def lengthOfLastWord(self, s):
        ls = len(s)
        # slow and fast pointers
        slow = -1
        # iterate over trailing spaces
        while slow >= -ls and s[slow] == ' ':
            slow -= 1
        
        fast = slow
        # iterate over last word
        while fast >= -ls and s[fast] != ' ':
            fast-=1
        return slow - fast
        
s = "luffy is still joyboy"
obj = Solution()
print(obj.lengthOfLastWord(s))