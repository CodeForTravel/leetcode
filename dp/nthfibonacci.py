# class Solution:
#     def fib(self, N: int) -> int:
#         a, b, c = 1, 0, 0
#         for _ in range(n):
#             a, b, c = b, c, a + b + c
#         return c


class Solution(object):
    def tribonacci(self, n):
        a, b, c = 1, 0, 0
        for _ in range(n):
            a, b, c = b, c, a + b + c
        return c


n = 25
obj = Solution()
print(obj.tribonacci(n))
