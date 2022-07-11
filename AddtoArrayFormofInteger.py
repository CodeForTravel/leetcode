class Solution(object):
    # def addToArrayForm(self, num, k):
    #     """
    #     :type num: List[int]
    #     :type k: int
    #     :rtype: List[int]
    #     """
    #     num_str = "".join([str(x) for x in num])
    #     new_num = str(int(num_str) + k)
    #     new_num = [int(x) for x in new_num]
    #     return new_num

    
    # by taking 'k' itself as a carry
    def addToArrayForm(self, num, k):
        for i in range(len(num)-1, -1,-1):
            sum_dig = num[i] + k
            num[i] = sum_dig % 10
            k = sum_dig // 10

        while k:
            num.insert(0, k%10)
            k = k // 10
        return num

        
        

# num = [9,9,9]
# k = 9999999
num = [1,2,0,0]
k = 34
obj = Solution()
print(obj.addToArrayForm(num, k))