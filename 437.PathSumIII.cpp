/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:

    unordered_map<long long, int> prefix;
        int ans = 0;

        void dfs(TreeNode* node, long long currSum, int targetSum){
            if (node == nullptr){
                return;
            }
            
            currSum += node->val;

            ans += prefix[currSum - targetSum];
            
            prefix[currSum]++;

            dfs(node->left, currSum, targetSum);
            dfs(node->right, currSum, targetSum);

            prefix[currSum]--;
        }



    int pathSum(TreeNode* root, int targetSum) {

        prefix[0] = 1;

        dfs(root, 0, targetSum);

        return ans;

        
        

        
    }
};