class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int c=0;
        int z=0;
        int l=0;
        int r=0;
        while (r< nums.size()){
            if (nums[r]==0){
                z++;
            }
            if (z>k){
                if (nums[l]==0){
                    z--;
                }
                l++;
            }
            if (z<=k){
                c=max(c,r-l+1);
            }
            r++;
        }

        return c;
        
    }
};