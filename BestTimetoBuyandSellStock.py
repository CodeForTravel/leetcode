class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfix = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfix =  max(profit, maxProfix)
            else:
                l = r
            r += 1
        return maxProfix


prices = [7,1,5,3,6,4]
obj = Solution()
print(obj.maxProfit(prices))