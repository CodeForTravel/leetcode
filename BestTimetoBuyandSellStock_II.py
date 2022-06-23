class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        totalProfix = 0

        # l, r = 0, 1
        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #         profit = prices[r] - prices[l]
        #         totalProfix += profit

        #     l = r
        #     r += 1
        # return totalProfix

        # another solution
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                totalProfix += prices[i] - prices[i-1]
        return totalProfix


prices = [7,1,5,3,6,4]
# prices = [1,2,3,4,5]
# prices = [7,6,4,3,1]
obj = Solution()
print(obj.maxProfit(prices))