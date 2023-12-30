class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        end = len(s) - 1
        while start <= end and s[start] == " ":
            start += 1
        while end >= start and s[end] == " ":
            end -= 1

        s = s[start : end + 1]
        words = s.split()  # Tokenize the string into words
        output = ""
        for k in range(len(words) - 1, 0, -1):
            output += words[k] + " "

        output += words[0]
        return output


s = "  the  sky is blue "

ser = Solution()
print(ser.reverseWords(s))
