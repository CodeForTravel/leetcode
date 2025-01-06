# 1769. Minimum Number of Operations to Move All Balls to Each Box
class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        res_list = []
        non_empty_box = []
        for index, value in enumerate(boxes):
            if value == "1":
                non_empty_box.append(index)

        for i in range(len(boxes)):
            couter = 0
            for j in non_empty_box:
                couter += abs(i - j)
            res_list.append(couter)
        return res_list


# boxes = "110"
boxes = "001011"
sol = Solution()
print(sol.minOperations(boxes))
