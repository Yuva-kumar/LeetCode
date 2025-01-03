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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>>res;
        if(root==NULL) return res;
        queue<TreeNode*>qu;
        qu.push(root);
        int kk=0;
        while(!qu.empty()){
            vector<int>v;
            int k=qu.size();
            for(int i=0;i<k;i++){
                TreeNode* temp;
                temp=qu.front();
                qu.pop();
                v.push_back(temp->val);
                if(temp->left !=NULL){
                    qu.push(temp->left);
                }
                if(temp-> right !=NULL){
                    qu.push(temp->right);
                }
            }
            if (kk==0){
                res.push_back(v);
                kk=1;
            }
            else{
                reverse(v.begin(),v.end());
                res.push_back(v);
                kk=0;
            }
            
        }
        return res;
        
    }
};