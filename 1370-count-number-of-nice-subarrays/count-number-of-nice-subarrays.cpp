class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        vector<int>v;
        for(auto it:nums){
            if (it %2!=0){
                v.push_back(1);
            }
            else{
                v.push_back(0);
            }
        }
        unordered_map<int,int>mpp;
        mpp[0]=1;
        int c=0,d=0;
        for(auto it:v){
            c+=it;
            int a=c-k;
            d+=mpp[a];
            mpp[c]++;
        }
        return d;

    }
};