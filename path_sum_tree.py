""""
Given the root of a binary tree and an integer targetSum, 
return true if the tree has a root-to-leaf path such that 
adding up all the values along the path equals targetSum.
A leaf is a node with no children.
"""
class Solution:
    def traversal(self, node):
        # condition for root node
        if not node.left and not node.right:
            if self.sum + node.val == self.target:
                self.output = True
        # condition for non-root node
        self.sum += node.val
        if node.left:
            self.traversal(node.left)
        if node.right:
            self.traversal(node.right)
        self.sum -= node.val
        
        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        self.sum = 0
        self.output = False
        self.target = targetSum
        self.traversal(root)
        return self.output