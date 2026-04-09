# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def lca(root,p,q):

            if root is p:
                return p
            
            if root is q:
                return q

            if root is None:
                return

            if p.val > root.val and q.val > root.val:
                right = lca(root.right,p,q)
                return right

            if p.val < root.val and q.val < root.val:
                left = lca(root.left,p,q)
                return left
            
            return root

        return lca(root,p,q)
        