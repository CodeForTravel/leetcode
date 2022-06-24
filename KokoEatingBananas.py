import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        l, r = 1, max(piles)
        result = r

        while l <= r:
            k = (l+r )// 2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)

            if hours <= h:
                result = min(k, result)
                r = k - 1
            else:
                l = k + 1
        return result
        


piles = [3,6,7,11]
h = 8
obj = Solution()
print(obj.minEatingSpeed(piles, h))