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
    vector<int> largestValues(TreeNode* root) {
        vector<int>res;
        if (root==NULL) return res;
   
        queue<TreeNode*>qu;
        qu.push(root);
        while(!qu.empty()){
            int a=INT_MIN;
            int k=qu.size();
            for(int i=0;i<k;i++){
                TreeNode* temp;
                temp=qu.front();
                qu.pop();
                a=max(a,temp->val);

                if(temp->left !=NULL){
                    qu.push(temp->left);
                }
                if(temp->right !=NULL){
                    qu.push(temp->right);
                }
            }
            res.push_back(a);
        }

        return res;
    }
};