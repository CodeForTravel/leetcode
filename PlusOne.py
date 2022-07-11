

# class Solution(object):
#     def plusOne(self, digits):
#         """
#         :type digits: List[int]
#         :rtype: List[int]
#         """
#         digits = digits[::-1]
#         digits.append(0) 

#         digits[0] = int(digits[0]) + 1

#         for i in range(len(digits)-1):
#             last_dig = digits[i] % 10
#             carry = digits[i] // 10
#             digits[i] = last_dig
#             digits[i+1] = digits[i+1] + carry
        
#         digits = digits[::-1]
#         i = 0
#         while i < len(digits) and digits[i] == 0:
#             i += 1

#         return digits[i:]


# another solution
# O(1) space, and O(1) time for most cases as well (with few chained 9's in the lower digits)
class Solution:
    def plusOne(self, digits):
        if not digits:
            return digits
        i = len(digits)-1
        digits[i] += 1
        while digits[i]==10:
            digits[i] = 0
            if i==0:
                digits.insert(0,1)
            else:
                digits[i-1] += 1
                i -= 1
        return digits
            

digits = [9,9,9]    
# digits = [4,3,2,1]
# digits = [9]
obj = Solution()
print(obj.plusOne(digits))