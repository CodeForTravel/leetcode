# 2657. Find the Prefix Common Array of Two Arrays


# class Solution(object):
#     def findThePrefixCommonArray(self, A, B):
#         """
#         :type A: List[int]
#         :type B: List[int]
#         :rtype: List[int]
#         """
#         set_a = set()
#         set_b = set()
#         res = []
#         for i in range(len(A)):
#             set_a.add(A[i])
#             set_b.add(B[i])
#             res.append(len(set_a) - len(set_a - set_b))
#         return res


class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        set_a = set()
        set_b = set()
        common_set = set()
        res = []
        for i in range(len(A)):
            set_a.add(A[i])
            set_b.add(B[i])
            if A[i] in set_b:
                common_set.add(A[i])
            if B[i] in set_a:
                common_set.add(B[i])
            res.append(len(common_set))
        return res


A = [1, 3, 2, 4]
B = [3, 1, 2, 4]

# A = [2, 3, 1]
# B = [3, 1, 2]
sol = Solution()
print(sol.findThePrefixCommonArray(A, B))
