# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # iterative bfs
        if not root:
            return 0
        depth = 1
        q = deque([(root, depth)])

        while q:
            node, val = q.popleft()

            if val > depth:
                depth = val

            if node.right:
                q.append((node.right, val + 1))
            if node.left:
                q.append((node.left, val + 1))
        
        return depth






