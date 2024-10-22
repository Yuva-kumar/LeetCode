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
    int maxLevelSum(TreeNode* root) {

        queue<TreeNode*>qu;
        qu.push(root);
        long long kk=LLONG_MIN;
        int res=0;
        int i=0;
        while(!qu.empty()){
            i++;
            int k=qu.size();
            long long s=0;
            for(int i=0;i<k;i++){
                TreeNode* a= qu.front();
                qu.pop();
                s+=a->val;
                if (a->left !=NULL){
                    qu.push(a->left);
                }
                if (a->right !=NULL){
                    qu.push(a->right);
                }
            }
            if (s>kk){
                kk=s;
                res=i;
            }
  
        }
        return res;      
        
    }
};