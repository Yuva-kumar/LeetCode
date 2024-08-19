class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int>mpp(256,-1);
        int l=0;
        int r=0;
        int res=0;
        while (r<s.size()){
            if (mpp[s[r]]!=-1){
                if (mpp[s[r]]>=l){
                    l=mpp[s[r]]+1;
                }

            }
            mpp[s[r]]=r;
            res=max(res,r-l+1);
            r++;
        }
        return res;
        
    }
};