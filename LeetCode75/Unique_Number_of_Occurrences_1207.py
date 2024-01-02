# class Solution(object):
#     def uniqueOccurrences(self, arr):
#         """
#         :type arr: List[int]
#         :rtype: bool
#         """

#         hash_dict = {}
#         for n in arr:
#             hash_dict[n] = hash_dict.get(n, 0) + 1

#         unique_occurance_set = set()
#         for occurance in hash_dict.values():
#             if occurance in unique_occurance_set:
#                 return False
#             else:
#                 unique_occurance_set.add(occurance)
#         return True


class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        hash_dict = {}
        for i in arr:
            if hash_dict.get(i):
                hash_dict[i] += 1
            else:
                hash_dict[i] = 1

        return len(hash_dict) == len(set(hash_dict.values()))


arr = [1, 2, 2, 1, 1, 3]
# arr = [1, 2]
sol = Solution()
print(sol.uniqueOccurrences(arr))
