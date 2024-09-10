class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        unordered_map<int,int>mpp;
        mpp[0]=1;
        int c=0,d=0;
        for(auto it:nums){
            c+=it%2;
            int a=c-k;
            d+=mpp[a];
            mpp[c]++;
        }
        return d;

    }
};