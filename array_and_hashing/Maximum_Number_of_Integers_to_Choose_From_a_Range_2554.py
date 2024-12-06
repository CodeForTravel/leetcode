class Solution(object):
    def maxCount(self, banned, n, maxSum):
        """
        :type banned: List[int]
        :type n: int
        :type maxSum: int
        :rtype: int
        """
        sub_sum = 0
        count = 0
        num_list = {i for i in range(1, n + 1)}

        for i in banned:
            num_list.discard(i)

        for i in num_list:
            if sub_sum + i <= maxSum:
                sub_sum += i
                count += 1
            else:
                return count
        return count


# banned = [1, 6, 5]
# n = 5
# maxSum = 6

# banned = [1, 2, 3, 4, 5, 6, 7]
# n = 8
# maxSum = 1

banned = [11]
n = 7
maxSum = 50
sol = Solution()
print(sol.maxCount(banned, n, maxSum))
