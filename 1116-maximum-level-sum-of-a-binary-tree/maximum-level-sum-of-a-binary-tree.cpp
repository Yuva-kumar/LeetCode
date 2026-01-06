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
        long long max_sum = LLONG_MIN;
        int res = 0;
        int i = 0;
        while(!qu.empty()){

            i++;
            int qu_size = qu.size();
            int curr_sum = 0;
            for(int j = 0; j < qu_size; j++ ){
                TreeNode* node = qu.front();
                curr_sum += node->val;
                qu.pop();

                if(node->left != NULL){
                    qu.push(node->left);
                }
                if(node->right != NULL){
                    qu.push(node->right);
                }

            }

            if(curr_sum > max_sum){
                max_sum = curr_sum;
                res = i;
            }

            
        }

        return res;        
    }
};