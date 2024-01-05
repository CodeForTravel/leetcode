# class Solution(object):
#     def decodeString(self, s):
#         stack = []
#         curNum = 0
#         curString = ""
#         for c in s:
#             if c == "[":
#                 stack.append(curString)
#                 stack.append(curNum)
#                 curString = ""
#                 curNum = 0
#             elif c == "]":
#                 num = stack.pop()
#                 prevString = stack.pop()
#                 curString = prevString + num * curString
#             elif c.isdigit():
#                 curNum = curNum * 10 + int(c)
#             else:
#                 curString += c
#         return curString


class Solution(object):
    def decodeString(self, s):
        stack = []
        for ch in s:
            if ch != "]":
                stack.append(ch)
            else:
                sub_string = ""
                while stack[-1] != "[":
                    sub_string = stack.pop() + sub_string
                # poping first Bracket
                stack.pop()
                # extracting number
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                # adding sub string back to stack by multiplying by number
                stack.append(int(num) * sub_string)
        return "".join(stack)


s = "3[a]2[bc]"
# s = "3[a2[c]]"
sol = Solution()
print(sol.decodeString(s))
