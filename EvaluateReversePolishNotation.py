class Solution(object):
    
    def evalRPN(self, tokens):
        stack = []
        for tok in tokens:
            if tok == '+':
                stack.append(stack.pop() + stack.pop())
            elif tok == '-':
                a, b = stack.pop() , stack.pop()
                stack.append(b-a)
            elif tok == '*':
                stack.append(stack.pop() * stack.pop())
            elif tok == '/':
                a, b = stack.pop() , stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(tok))

        return stack[0]
        

tokens = ["2","1","+","3","*"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
obj = Solution()
print(obj.evalRPN(tokens))