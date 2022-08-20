import heapq


class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        dis_point = []
        for x, y in points:
            dis = abs(((0-x)**2) + ((0-y)**2))
            dis_point.append([dis, x , y])

        heapq.heapify(dis_point)

        res = []
        for i in range(k):
            min_value = heapq.heappop(dis_point)
            res.append([min_value[1], min_value[2]])
        return res
        

list_items = [[3,3],[5,-1],[-2,4]]
obj = Solution()
print(obj.kClosest(list_items,2))