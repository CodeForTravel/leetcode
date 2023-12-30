# Sample Examples
# Strl = "AB"
# Str2 = "AB"

# Str1 = "ABABAB"
# Str2 = "ABAB"

# Str1 = "ABABABAB"
# Str2 = "ABAB"

# Str1 = "ABAB"
# Str2 = "ABABABAB"
# Conditions to fillup to get the greatest common divisor
# --------------------------------------------------------
# 1. Assuming str1 is always greater than the str2 to divide str1 by str2. So if str2 is greater than the str1, then swap the values.
# 2. If str1 == str2, then just simply return any of str1 and str2.
# 3. Check if the str1 is start with str2,  then recursively check apply the all condition over rest of the(where str2 end in str1) str1 and str2.


class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if len(str2) > len(str1):
            return self.gcdOfStrings(str2, str1)
        if str1 == str2:
            return str1

        if str1.startswith(str2):
            str2_len = len(str2)
            return self.gcdOfStrings(str1[str2_len:], str2)
        return ""


str1 = "ABABAB"
str2 = "ABAB"
ser = Solution()
print(ser.gcdOfStrings(str1, str2))
