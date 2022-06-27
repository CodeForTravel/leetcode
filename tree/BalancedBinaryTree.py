class Solution(object):
    # def isBalanced(self, root):

    #     if root is None: return True

    #     def traverse(root):
    #         if root is None: return 0

    #         left = traverse(root.left)
    #         right = traverse(root.right)
    #         diff  = abs(left - right)
            
    #         if diff > 1:
    #             return False
    #         return max(left, right) + 1
    #     traverse(root)
    #     return True

    def isBalanced(self, root):
        
        def dfs(root):
            if not root: return [True,0]
            
            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and 
                        abs(left[1] - right[1]) <= 1)
            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]