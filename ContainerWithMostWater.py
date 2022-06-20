class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result = 0
        l = 0
        r = len(height) - 1
        while l < r:
            pass
            width = r - l
            _height = min(height[r], height[l])
            area = width * _height
            result = max(result, area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return result


height = [1,8,6,2,5,4,8,3,7]
obj = Solution()
print(obj.maxArea(height))