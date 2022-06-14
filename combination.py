from itertools import combinations


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        num_list = [i for i in range(1, n+1)]
        comb = combinations(num_list, k)
        comb_list = []
        for i in comb:
            comb_list.append(list(i))
        return comb_list


obj = Solution()
print(obj.combine(4, 2))
