class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return pow(x,n)


obj = Solution()
x = 2.00000
n = 10
print(obj.myPow(x, n))