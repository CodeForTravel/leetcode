class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        new_srting = ""
        for i in s:
            if i == '-' or i.isdigit():
                new_srting += i
        return int(new_srting)
        


val = "__-42"
obj = Solution()
print(obj.myAtoi(val))