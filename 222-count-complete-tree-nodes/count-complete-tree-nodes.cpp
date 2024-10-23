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
int fun(TreeNode* root,int &k){
    if (root==NULL){
        return k;
    }
    k++;
    fun(root->left,k);
    fun(root->right,k);
    return k;
}
    int countNodes(TreeNode* root) {
        if (root==NULL)return 0;
        int k=0;
        return fun(root,k);
    }
};