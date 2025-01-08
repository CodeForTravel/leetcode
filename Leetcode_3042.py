class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        res = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                response = self.isPrefixAndSuffix(words[i], words[j])
                if response:
                    res += 1
        return res

    def isPrefixAndSuffix(self, str1, str2):
        # if str2.startswith(str1) and str2.endswith(str1):
        #     return True
        # else:
        #     return False

        if len(str1) > len(str2):
            return False

        len_ = len(str1)
        for i in range(len_):
            if str1[i] != str2[i] or str1[-(i + 1)] != str2[-(i + 1)]:
                return False
        return True


# words = ["a", "aba", "ababa", "aa"]
# words = ["pa", "papa", "ma", "mama"]
words = ["abc", "aba"]
sol = Solution()
print(sol.countPrefixSuffixPairs(words))
