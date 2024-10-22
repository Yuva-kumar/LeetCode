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
    long long kthLargestLevelSum(TreeNode* root, int k) {
        queue<TreeNode*>qu;
        qu.push(root);
        vector<long long>v;
        while(!qu.empty()){
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
            v.push_back(s);
        }

        sort(v.begin(),v.end(),greater<long long>());
        if (v.size()>=k){
            return v[k-1];
        }
        return -1;        
    }
};