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
    vector<double> averageOfLevels(TreeNode* root) {
        vector<double>v;
        if (root==NULL)return v;
        queue<TreeNode*>qu;
        qu.push(root);
        while(!qu.empty()){
            long long s=0;
            int x=0;
            int k=qu.size();
            for(int i=0;i<k;i++){
                TreeNode* a=qu.front();
                qu.pop();
                s+=a->val;
                x++;
                if(a->left!=NULL){
                    qu.push(a->left);
                }
                if(a->right!=NULL){
                    qu.push(a->right);
                }
            }
            double res=static_cast<double>(s)/x;
            v.push_back(res);
        }

        return v;
        
    }
};