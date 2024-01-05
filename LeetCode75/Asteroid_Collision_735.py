class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        res_stack = []
        for a in asteroids:
            while res_stack and a < 0 and res_stack[-1] > 0:
                diff = a + res_stack[-1]
                if diff > 0:
                    a = 0
                elif diff < 0:
                    res_stack.pop()
                else:
                    a = 0
                    res_stack.pop()
            if a:
                res_stack.append(a)
        return res_stack


asteroids = [5, 10, -5]
asteroids = [8, -8]
asteroids = [-2, -1, 1, 2]
ser = Solution()
print(ser.asteroidCollision(asteroids))
