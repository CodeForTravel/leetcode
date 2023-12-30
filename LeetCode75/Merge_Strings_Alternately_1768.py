class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res = ""

        min_length = min(len(word1), len(word2))
        for i in range(min_length):
            res += word1[i] + word2[i]

        if len(word1) > min_length:
            res += word1[min_length:]

        if len(word2) > min_length:
            res += word2[min_length:]
        return res


word1 = "abcd"
word2 = "pq"
ser = Solution()
print(ser.mergeAlternately(word1, word2))
