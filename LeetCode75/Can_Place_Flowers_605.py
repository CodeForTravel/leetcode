class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        for i in range(len(flowerbed)):
            if i == len(flowerbed) - 1 and flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                flowerbed[i] = 1
                n -= 1
                continue

            if i == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
                continue

            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1

        if n > 0:
            return False
        return True


# flowerbed = [1, 0, 0, 0, 0, 1]
# flowerbed = [0, 0, 1, 0, 1]

flowerbed = [1, 0, 0, 0, 1, 0, 0]
n = 2
ser = Solution()
print(ser.canPlaceFlowers(flowerbed, n))


# Wrong for some cases. Case passed  114
# class Solution(object):
#     def canPlaceFlowers(self, flowerbed, n):
#         """
#         :type flowerbed: List[int]
#         :type n: int
#         :rtype: bool
#         """
#         is_previous_number_zero = False
#         for i in flowerbed:
#             if i == 1:
#                 is_previous_number_zero = False
#             elif i == 0 and is_previous_number_zero:
#                 n -= 1
#                 is_previous_number_zero = False
#             else:
#                 is_previous_number_zero = True

#         if n > 0:
#             return False
#         return True


# better solution
class BetterSolution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        possible_to_place_counter = 0
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 0 and flowerbed[i - 1] != 1 and flowerbed[i + 1] != 1:
                possible_to_place_counter += 1
                flowerbed[i] = 1
        return possible_to_place_counter >= n
