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
    
    long long res = 0;
    long long totalsum = 0;

    long long getTotalSum(TreeNode* root){
        if(!root) return 0;
        return root->val + getTotalSum(root->left) + getTotalSum(root->right);
    }

    long long dfsTraversal(TreeNode* root){
        
        if(!root) return 0;

        long long left = dfsTraversal(root->left);
        long long right = dfsTraversal(root->right);

        long long currentSum = root->val + left + right;

        res = max((totalsum-currentSum)*currentSum,res);

        return currentSum;
    }

    int maxProduct(TreeNode* root) {
        totalsum = getTotalSum(root);
        dfsTraversal(root);

        return res % 1000000007LL;

    }
};