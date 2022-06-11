class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # temp = x
        # reverse_num = 0
        # while(x > 0):
        #     remider = x % 10
        #     reverse_num = (reverse_num*10)+remider
        #     x = x // 10
        # return reverse_num == temp

        # better solution form leetcode
        return str(x)[::-1] == str(x)


obj = Solution()
print(obj.isPalindrome(56))
print(obj.isPalindrome(121))
