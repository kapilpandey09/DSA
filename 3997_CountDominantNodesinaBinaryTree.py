# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countDominantNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        ans = [0]

        def dfs(node):
            

            if not node:
                return float("-inf")

            lm = dfs(node.left)
            rm = dfs(node.right)

            mx = max(node.val, lm, rm)

            if node.val == mx:
                ans[0] += 1

            return mx

        dfs(root)
        return ans[0]
        
            
        
        