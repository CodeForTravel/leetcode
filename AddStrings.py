# class Solution(object):
#     def addStrings(self, num1, num2):
#         carry = 0
#         res = ""
#         num1 = list(num1)
#         num2 = list(num2)
 
#         while num1 or num2:
#             if num1:
#                 carry += int(num1.pop())
#             if num2:
#                 carry += int(num2.pop())
#             res = res + str(carry % 10)
#             carry = carry // 10

#         while carry:
#             res = res + str(carry % 10)
#             carry = carry // 10

#         return res[::-1]


# using dict
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        def str2int(num):
            numDict = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5,
                  '6' : 6, '7' : 7, '8' : 8, '9' : 9}
            output = 0
            for d in num:
                output = output * 10 + numDict[d]
            return output
        return str(str2int(num1) + str2int(num2))

# Use of unicode
# class Solution:
#     def addStrings(self, num1: str, num2: str) -> str:
#         def str2int(num):
#             result  = 0
#             for n in num:
#                 result = result * 10 + ord(n) - ord('0')
#             return result
#         return str(str2int(num1) + str2int(num2))

num1 = "9433"
num2 = "1343"
obj = Solution()
print(obj.addStrings(num1, num2))


