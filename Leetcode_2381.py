class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        prefix_diff = [0] * (len(s) + 1)
        for left, right, direction in shifts:
            prefix_diff[right + 1] += 1 if direction else -1
            prefix_diff[left] += -1 if direction else 1

        diff = 0
        res = [ord(c) - ord("a") for c in s]
        for i in reversed(range(len(prefix_diff))):
            diff += prefix_diff[i]
            res[i - 1] = (diff + res[i - 1] + 26) % 26

        s = [chr(ord("a") + n) for n in res]
        return "".join(s)


# Test the solution
s = "abc"
shifts = [[0, 1, 0], [1, 2, 1], [0, 2, 1]]
sol = Solution()
print(sol.shiftingLetters(s, shifts))
