class Solution:
    def topKFrequent(self, nums, k):

        hashDict = {}
        for i in nums:
            hashDict[i] = hashDict.get(i, 0) + 1

        hashDict = {k: v for k, v in sorted(
            hashDict.items(), key=lambda item: item[1], reverse=True)}

        new_list = []
        count = 0
        for key in hashDict.keys():
            count += 1
            new_list.append(int(key))
            if count == k:
                break
        return new_list


# nums = [1, 1, 1, 2, 2, 3]
# k = 2
# nums = [1]
# k = 1


nums = [4, 1, -1, 2, -1, 2, 3]
k = 2

obj = Solution()
print(obj.topKFrequent(nums, k))
