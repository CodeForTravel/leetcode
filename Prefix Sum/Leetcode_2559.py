# 2559. Count Vowel Strings in Ranges
class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        vowels = ("a", "e", "i", "o", "u")
        prefix_count = [0] * (len(words) + 1)

        counter = 0
        for index, word in enumerate(words):
            if word[0] in vowels and word[-1] in vowels:
                counter += 1
            prefix_count[index + 1] = counter

        result = []
        for start, end in queries:
            result.append(prefix_count[end + 1] - prefix_count[start])
        return result


# words = ["aba", "bcb", "ece", "aa", "e"]
# queries = [[0, 2], [1, 4], [1, 1]]

words = ["a", "e", "i"]
queries = [[0, 2], [0, 1], [2, 2]]

sol = Solution()
print(sol.vowelStrings(words, queries))
