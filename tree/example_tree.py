# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)
node_4 = TreeNode(4)
node_5 = TreeNode(5)
# node_6 = TreeNode(6)
node_7 = TreeNode(7)


node_1.left = node_2
node_1.right = node_3

node_2.left = node_4
node_2.right = node_5


node_3.right = node_7


