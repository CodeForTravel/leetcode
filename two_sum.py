class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # found_values = set()
        # last_num_index = -1
        # first_number = -1
        # first_num_index = -1
        # is_number_found = False
        # for i, a in enumerate(nums):
        #     diff = target - a
        #     if diff in found_values:
        #         is_number_found = True
        #         last_num_index = i
        #         first_number = diff
        #         break
        #     found_values.add(a)

        # first_num_index = nums.index(first_number)
        # if is_number_found:
        #     return [first_num_index, last_num_index]

        # better soution
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            else:
                prevMap[n] = i


value_list = [2, 7, 11, 15]
target = 9

obj = Solution()
print(obj.twoSum(value_list, target))
