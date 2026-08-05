# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        def dfs(root): #get heights for indiv branches
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            if abs(left-right) > 1:
                self.balanced = False
            # get branch height
            return 1 + max(left, right)
        
        dfs(root)
        return self.balanced