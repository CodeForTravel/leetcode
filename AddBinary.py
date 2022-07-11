class Solution(object):
    # def addBinary(self, a, b):
    #     """
    #     :type a: str
    #     :type b: str
    #     :rtype: str
    #     """
    #     sum_ = int(a,2) + int(b, 2)
    #     out = []
    #     if sum_ <= 0:
    #         return "0"

    #     while sum_ > 0:
    #         out.append(str(sum_ % 2))
    #         sum_ = sum_ // 2
    #     return "".join(out[::-1])


    # without using built in function
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ''

        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            result += str(carry %2)
            carry //= 2

        return result[::-1]
        

a = "0"
b = "0"
obj = Solution()
print(obj.addBinary(a,b))