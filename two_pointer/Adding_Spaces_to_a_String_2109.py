class Solution(object):
    def addSpaces(self, s, spaces):
        """
        :type s: str
        :type spaces: List[int]
        :rtype: str
        """
        result = []
        prev_index = 0

        for space_index in spaces:
            result.append(s[prev_index:space_index])
            result.append(" ")
            prev_index = space_index

        result.append(s[prev_index:])
        return "".join(result)


s = "LeetcodeHelpsMeLearn"
spaces = [8, 13, 15]

s = "spacing"
spaces = [0, 1, 2, 3, 4, 5, 6]
sol = Solution()
print(sol.addSpaces(s, spaces))
