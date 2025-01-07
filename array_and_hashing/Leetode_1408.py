# 1408. String Matching in an Array


class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = set()
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i] in words[j]:
                    res.add(words[i])
                elif words[j] in words[i]:
                    res.add(words[j])

        return list(res)


words = ["mass", "as", "hero", "superhero"]
sol = Solution()
print(sol.stringMatching(words))
