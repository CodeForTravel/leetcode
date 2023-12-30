class Solution(object):
    def maxArea(self, height):
        res = 0
        start, end = 0, len(height) - 1
        while start < end:
            width = end - start
            height_ = min(height[start], height[end])
            area = width * height_
            res = max(area, res)

            if height[end] > height[start]:
                start += 1
            else:
                end -= 1
        return res


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
sol = Solution()
print(sol.maxArea(height))
