class Solution(object):
    def reverseVowels(self, s):
        vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")

        s_list = [i for i in s]
        start = 0
        end = len(s_list) - 1
        while start < end:
            if s_list[end] not in vowels:
                end -= 1
            elif s_list[start] not in vowels:
                start += 1
            else:
                temp = s_list[start]
                s_list[start] = s_list[end]
                s_list[end] = temp
                end -= 1
                start += 1
        return "".join(s_list)


s = "hello"
ser = Solution()
print(ser.reverseVowels(s))
