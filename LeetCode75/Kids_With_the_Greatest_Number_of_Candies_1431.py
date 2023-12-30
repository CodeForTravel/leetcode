class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        greatest_number_of_candies = self.find_greatest_number_of_list(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= greatest_number_of_candies:
                candies[i] = True
            else:
                candies[i] = False
        return candies

    def find_greatest_number_of_list(self, number_list):
        if not number_list:
            return None

        start = 0
        end = len(number_list) - 1
        greatest_number = 0
        while start <= end:
            if greatest_number < number_list[start]:
                greatest_number = number_list[start]

            if greatest_number < number_list[end]:
                greatest_number = number_list[end]

            start += 1
            end -= 1
        return greatest_number


candies = [2, 3, 5, 1, 3]
extraCandies = 3

ser = Solution()
print(ser.kidsWithCandies(candies, extraCandies))
