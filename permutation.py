
from itertools import permutations


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permutation_list = []
        perm = permutations(nums)
        for i in perm:
            permutation_list.append(list(i))
        return permutation_list


new_list = [1, 2, 3]
obj = Solution()
print(obj.permute(new_list))
