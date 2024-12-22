class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        least_avg_index = {"index": 0, "avg": classes[0][0] / classes[0][1]}
        sum_of_avg = 0
        for index, pair in enumerate(classes):
            avg = pair[0] / pair[1]
            sum_of_avg += avg
            if least_avg_index["avg"] > avg:
                least_avg_index["avg"] = avg
                least_avg_index["index"] = index

        sum_of_avg = sum_of_avg - (classes[least_avg_index["index"]][0] / classes[least_avg_index["index"]][1])
        sum_of_avg = sum_of_avg + (
            (classes[least_avg_index["index"]][0] + extraStudents)
            / (classes[least_avg_index["index"]][1] + extraStudents)
        )

        avg = sum_of_avg / len(classes)
        return round(avg, 5)


classes = [[3, 5], [2, 2], [1, 2]]
extraStudents = 2
# classes = [[2, 4], [3, 9], [4, 5], [2, 10]]
# extraStudents = 4
sol = Solution()
print(sol.maxAverageRatio(classes, extraStudents))
