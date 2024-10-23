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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>>v;
        if (root==NULL)return v;
        queue<TreeNode*>qu;
        qu.push(root);
        while(!qu.empty()){
            vector<int>v1;
            int k=qu.size();
            for(int i=0;i<k;i++){
                TreeNode* a=qu.front();
                qu.pop();
                v1.push_back(a->val);
                if(a->left!=NULL){
                    qu.push(a->left);
                }
                if(a->right!=NULL){
                    qu.push(a->right);
                }
            }
            v.push_back(v1);
        }
        vector<vector<int>>res;
        int k=v.size();
        for(int i=0;i<v.size();i++){
            res.push_back(v[k-i-1]);
        }

        return res;
    }
};