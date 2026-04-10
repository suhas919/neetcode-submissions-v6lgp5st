# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:


        def maxSum(root):

            if root is None:
                return 0

            left = maxSum(root.left) 

            right = maxSum(root.right)

            return max(root.val + max(left,right),0)


        res = -float('inf')
        node = root

        def inorder(root):
            nonlocal res
            if not root:
                return
            res = max(res, root.val+maxSum(root.left)+maxSum(root.right))
            inorder(root.left)
            inorder(root.right)

        inorder(root)

        return res


        