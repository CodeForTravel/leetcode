class Solution(object):
    def canChange(self, start, target):
        """
        :type start: str
        :type target: str
        :rtype: bool
        """
        if start.replace("_", "") != target.replace("_", ""):
            return False

        j = 0
        for i, c in enumerate(start):
            if c == "L":
                while target[j] != "L":
                    j += 1
                if i < j:
                    return False
                j += 1

        j = 0
        for i, c in enumerate(start):
            if c == "R":
                while target[j] != "R":
                    j += 1
                if i > j:
                    return False
                j += 1
        return True


# Example usage
start = "_L__R__R_"
target = "L______RR"
sol = Solution()
print(sol.canChange(start, target))
