# 2425. Bitwise XOR of All Pairings


class Solution(object):
    def xorAllNums(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        xor1 = 0
        xor2 = 0

        # XOR all elements in nums1 and nums2
        for num in nums1:
            xor1 ^= num
        for num in nums2:
            xor2 ^= num

        # Determine the result based on the counts
        result = 0
        if len(nums2) % 2 == 1:  # nums2 contributes xor1 if its size is odd
            result ^= xor1
        if len(nums1) % 2 == 1:  # nums1 contributes xor2 if its size is odd
            result ^= xor2

        return result


nums1 = [2, 1, 3]
nums2 = [10, 2, 5, 0]

nums1 = [1, 2]
nums2 = [3, 4]
sol = Solution()
print(sol.xorAllNums(nums1, nums2))
