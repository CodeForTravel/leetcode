class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        words = sentence.split()
        for i, word in enumerate(words):
            if word.startswith(searchWord):
                return i + 1
        return -1


sentence = "i love eating burger"
searchWord = "burg"
sentence = "this problem is an easy problem"
searchWord = "pro"
sol = Solution()
print(sol.isPrefixOfWord(sentence, searchWord))
