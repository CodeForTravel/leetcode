class Solution:
    def fib(self, N: int) -> int:
        a, b = 0, 1
        for i in range(N):
            a, b = b, a + b
        return a


n = 4
obj = Solution()
print(obj.fib(n))
