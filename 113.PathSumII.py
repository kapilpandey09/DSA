# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        ans = []
        def dfs(root, arr, currS):

            if not root:
                return 

            arr.append(root.val)
            currS+=root.val


            if not root.left and not root.right:
                if currS == targetSum:
                    ans.append(arr.copy())

            
            dfs(root.left, arr, currS)
            dfs(root.right, arr, currS)

            arr.pop()
        
        dfs(root, [], 0)

        return ans

                 