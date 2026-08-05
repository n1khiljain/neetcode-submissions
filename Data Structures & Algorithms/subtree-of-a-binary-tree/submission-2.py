# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root1, root2):
            if root1 is None and root2 is None:
                return True
            
            if root1 is None or root2 is None:
                return False
            
            if root1.val != root2.val:
                return False

            return (sameTree(root1.left, root2.left) and 
                sameTree(root1.right, root2.right)
            )
        
        q = deque([(root, subRoot)])

        while q:
            root, root2 = q.popleft()

            if sameTree(root, root2):
                return True
            if root.left is not None:
                q.append((root.left, root2))
            if root.right is not None:
                q.append((root.right, root2))
            
            
        return False