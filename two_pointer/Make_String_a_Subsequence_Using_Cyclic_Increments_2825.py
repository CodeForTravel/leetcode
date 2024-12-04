class Solution(object):
    def canMakeSubsequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        result = False
        i, j = 0, 0
        while i < len(str1) and j < len(str2):
            next_char_value = self.get_next_ascii_value(str1[i])
            if str1[i] == str2[j]:
                j += 1
            elif next_char_value == ord(str2[j]):
                j += 1
            i += 1

            if j == len(str2):
                return True
        return result

    def get_next_ascii_value(self, char):
        current_value = ord(char)
        if current_value == 122:  # ASCII value of 'z'
            return 97  # ASCII value of 'a'
        else:
            return current_value + 1


# str1 = "abc"
# str2 = "ad"
# str1 = "zc"
# str2 = "ad"
str1 = "ab"
str2 = "d"
sol = Solution()
print(sol.canMakeSubsequence(str1, str2))
