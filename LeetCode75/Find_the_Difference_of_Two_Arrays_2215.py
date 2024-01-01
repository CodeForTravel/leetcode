class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        output = [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]
        return output


nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
nums1 = [1, 2, 3, 3]
nums2 = [1, 1, 2, 2]
sol = Solution()
print(sol.findDifference(nums1, nums2))
