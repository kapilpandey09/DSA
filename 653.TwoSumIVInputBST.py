# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        tree = set()

        def search(node):
            
            if not node:
                return False

            if k - node.val in tree:
                return True
            
            tree.add(node.val)

            return search(node.left) or search(node.right)

        return search(root)

        
        