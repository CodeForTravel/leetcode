# Leetcode: 916 Word Subsets
from collections import Counter


class Solution(object):
    def wordSubsets(self, words1, words2):
        # Get the maximum count of each character required by all words in words2
        count_b = Counter()
        for word in words2:
            count_word = Counter(word)
            for letter in count_word:
                count_b[letter] = max(count_b[letter], count_word[letter])

        # Now, check each word in words1 if it contains all the required letters
        result = []
        for word in words1:
            count_a = Counter(word)
            if all(count_a[letter] >= count_b[letter] for letter in count_b):
                result.append(word)

        return result


words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["e", "o"]

# words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
# words2 = ["e", "oo"]

words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["lo", "eo"]
# ["google","leetcode"]

# dict_ = {"l": 1, "o": 1}

# l, o e o


sol = Solution()
print(sol.wordSubsets(words1, words2))
