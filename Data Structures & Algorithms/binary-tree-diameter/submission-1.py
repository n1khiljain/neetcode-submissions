# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter is sum of left tree + right tree
        if not root:
            return 0

        def getMaxHeight(root):
            if not root:
                return 0
            
            leftMax = getMaxHeight(root.left)
            rightMax = getMaxHeight(root.right)
            return 1 + max(leftMax, rightMax)

        return max(getMaxHeight(root.left) + getMaxHeight(root.right), 
                self.diameterOfBinaryTree(root.left),
                self.diameterOfBinaryTree(root.right)
                )
        

        

        