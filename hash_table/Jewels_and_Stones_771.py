class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        # hash_map = [x for x in jewels]
        hash_map = {}
        for i in jewels:
            hash_map[i] = 0
        res = 0
        for k in stones:
            if k in hash_map:
                res += 1
        return res

jewels = "aA"
stones = "aAAbbbb"
# jewels = "z"
# stones = "ZZ"
obj = Solution()
print(obj.numJewelsInStones(jewels, stones))