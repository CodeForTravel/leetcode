class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) != len(word2):
            return False

        if set(word1) != set(word2):
            return False

        hash_dict1 = {}
        hash_dict2 = {}
        for i in range(len(word1)):
            hash_dict1[word1[i]] = hash_dict1.get(word1[i], 0) + 1
            hash_dict2[word2[i]] = hash_dict2.get(word2[i], 0) + 1

        return sorted(hash_dict1.values()) == sorted(hash_dict2.values())


word1 = "abc"
word2 = "bca"
sol = Solution()
print(sol.closeStrings(word1, word2))
