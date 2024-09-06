class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int,int>mpp;
        mpp[0]=1;
        int a=0,b=0;
        for(auto it:nums){
            a+=it;
            int diff=a-k;
            b+=mpp[diff];
            mpp[a]++;
        }
        return b;
    }
};