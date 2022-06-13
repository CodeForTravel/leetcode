class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest_word = min(strs, key=len)
        for i, char in enumerate(shortest_word):
            for other_order in strs:
                if other_order[i] != char:
                    return shortest_word[:i]
        return shortest_word


# strs = ["flower", "flow", "flight"]
# obj = Solution()
# print(obj.longestCommonPrefix(strs))
