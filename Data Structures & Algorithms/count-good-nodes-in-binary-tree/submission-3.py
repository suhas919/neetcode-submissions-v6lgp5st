# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if root is None:
            return 0

        def gn(root, prevMax):
            if root is None:
                return 0
            
            # if root.val >= prevMax:
            left = 0
            right = 0
            res = 0
            print("Node = ", root.val)
            if root.left:
                left = gn(root.left, max(prevMax, root.left.val))
                if root.left.val >= prevMax:
                    print("Increminting, cur_max = ",prevMax )
                    res+=1
            if root.right:
                right = gn(root.right, max(prevMax, root.right.val))
                if root.right.val >= prevMax:
                    print("Increminting, cur_max = ",prevMax )
                    res+=1
            return res + left + right

        res = 1 + gn(root, root.val)


        return res
        