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
void fun(vector<int>&v,TreeNode* root){
    if (root==NULL)return;
    fun(v,root->left);
    fun(v,root->right);
    v.push_back(root->val);

}
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int>v;
        fun(v,root);
        return v;
        
    }
};