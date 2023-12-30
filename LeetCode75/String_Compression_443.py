class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = 0
        i = 0

        while i < len(chars):
            letter = chars[i]
            count = 0
            while i < len(chars) and chars[i] == letter:
                count += 1
                i += 1
            # adding character to list
            chars[ans] = letter
            ans += 1
            # adding count to list
            if count > 1:
                for c in str(count):
                    chars[ans] = c
                    ans += 1
        return ans


chars = ["a", "a", "b", "b", "c", "c", "c"]
# chars = ["a"]
ser = Solution()
print(ser.compress(chars))
