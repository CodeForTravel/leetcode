# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        res = [False]
        def preorder_traversal(root_):
            if root_:
                if isSameTree(root_, subRoot):
                    res[0] = True
                preorder_traversal(root_.left)
                preorder_traversal(root_.right)

        def isSameTree(p,q):
            if not p and not q: return True
            if p and q and p.val == q.val: 
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
            else: return False
        
        preorder_traversal(root)
        return res[0]


# another solution ===============
class Solution:
    def isSubtree(self, s, t):
        if not t: return True
        if not s: return False
        
        if self.sameTree(s, t):
            return True
        return (self.isSubtree(s.left, t) or
                self.isSubtree(s.right, t))
    
    def sameTree(self, s, t):
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return (self.sameTree(s.left, t.left) and
                    self.sameTree(s.right, t.right))
        return False