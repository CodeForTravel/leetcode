class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowel_dict = {"a": "a", "e": "e", "i": "i", "o": "o", "u": "u"}

        vowel_count = 0
        for i in range(k):
            if vowel_dict.get(s[i]):
                vowel_count += 1
        max_vowel = vowel_count

        start = 0
        end = k

        while end < len(s):
            if vowel_dict.get(s[start]):
                vowel_count -= 1
            start += 1

            if vowel_dict.get(s[end]):
                vowel_count += 1
            end += 1

            max_vowel = max(max_vowel, vowel_count)
        return max_vowel


s = "abciiidef"
k = 3
ser = Solution()
print(ser.maxVowels(s, k))
