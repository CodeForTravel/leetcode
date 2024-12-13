import math


class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(k):
            gifts.sort()
            # print(gifts)
            gifts[-1] = math.floor(math.sqrt(gifts[-1]))
        return int(sum(gifts))


gifts = [25, 64, 9, 4, 100]
k = 4
sol = Solution()
print(sol.pickGifts(gifts, k))
