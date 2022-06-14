
class Solution(object):
    def groupAnagrams(self, strs):
        if len(strs) == 1:
            return [strs]

        hashDict = {}
        for item in strs:
            sorted_list = sorted(item)
            sorted_string = "".join(sorted_list)
            if hashDict.get(sorted_string):
                hashDict[sorted_string].append(item)
            else:
                hashDict[sorted_string] = [item]

        result_list = []
        for value in hashDict.values():
            result_list.append(value)

        return result_list


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
strs = ["a"]
strs = [""]
obj = Solution()
print(obj.groupAnagrams(strs))
