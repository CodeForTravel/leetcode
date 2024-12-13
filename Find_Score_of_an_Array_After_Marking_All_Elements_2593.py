class Solution(object):
    def findScore(self, nums):

        # Convert the numbers into a list of (value, index) pairs
        pairs = [(nums[i], i) for i in range(len(nums))]

        # Sort the pairs by value, and then by index
        pairs.sort(key=lambda x: (x[0], x[1]))

        # Initialize a set to track marked indices and a score counter
        marked_indices = set()
        score = 0

        # Process each pair in the sorted list
        for value, idx in pairs:
            # If this index is already marked, skip
            if idx in marked_indices:
                continue

            # Add the value to the score
            score += value

            # Mark this index and its neighbors (if they exist)
            marked_indices.add(idx)
            if idx > 0:
                marked_indices.add(idx - 1)
            if idx < len(nums) - 1:
                marked_indices.add(idx + 1)
        return score


nums = [2, 1, 3, 4, 5, 2]
sol = Solution()
print(sol.findScore(nums))
