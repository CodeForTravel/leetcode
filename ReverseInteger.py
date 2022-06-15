from sys import flags


class Solution(object):
    def reverse(self, x):

        # if x >= 0:
        #     reserse_num = int(str(x)[::-1])
        # else:
        #     x = str(x)[1::1]
        #     reserse_num = int('-' + x[::-1])

        # # print(reserse_num.bit_length())
        # if reserse_num.bit_length() >= 32:
        #     return 0
        # return reserse_num

        numFlag = 1

        if x < 0:
            numFlag = -1
            x = str(-x)
        else:
            x = str(x)
        x = int(x[::-1])

        return 0 if x > pow(2, 31) else x * numFlag


n = 163847412
obj = Solution()
print(obj.reverse(n))
