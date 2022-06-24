class Solution(object):
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures)
        stack = [] 

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                res[stackIndex] = i - stackIndex
            stack.append([temp, i])
        return res
        

temperatures = [73,74,75,71,69,72,76,73]
obj = Solution()
print(obj.dailyTemperatures(temperatures))