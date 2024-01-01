class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        max_gain = 0
        gain = [0] + gain

        for i in range(1, len(gain)):
            current_gain = gain[i - 1] + gain[i]
            max_gain = max(max_gain, current_gain)
            gain[i] = current_gain
        return max_gain


# gain = [-5, 1, 5, 0, -7]
# gain = [-4, -3, -2, -1, 4, 3, 2]
# gain = [52, -91, 72]
gain = [
    44,
    32,
    -9,
    52,
    23,
    -50,
    50,
    33,
    -84,
    47,
    -14,
    84,
    36,
    -62,
    37,
    81,
    -36,
    -85,
    -39,
    67,
    -63,
    64,
    -47,
    95,
    91,
    -40,
    65,
    67,
    92,
    -28,
    97,
    100,
    81,
]

ser = Solution()
print(ser.largestAltitude(gain))
