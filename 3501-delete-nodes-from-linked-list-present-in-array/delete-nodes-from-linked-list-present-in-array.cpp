/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* modifiedList(vector<int>& nums, ListNode* head) {
        // int m=*max_element(nums.begin(),nums.end());
        vector<int>v(100000+1,0);
        for(auto it:nums){
            v[it]=1;
        }
        ListNode* temp=new ListNode();
        ListNode* res=temp;
        while (head!=nullptr){
            int k=head->val;
            if(v[k]==0){
                temp->next=new ListNode(k);
                temp=temp->next;
            }
            head=head->next;
        }
        return res->next;
        
    }
};