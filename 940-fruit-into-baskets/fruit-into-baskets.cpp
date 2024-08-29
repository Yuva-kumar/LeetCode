class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        int l=0,r=0,res=0;
        unordered_map<int,int>mpp;
        while (r< fruits.size()){
            mpp[fruits[r]]++;

            if(mpp.size()>2){
                mpp[fruits[l]]--;
                if (mpp[fruits[l]]==0){
                    mpp.erase(fruits[l]);
                }
                l++;
            }

            res=max(res,r-l+1);
            r++;
        }
        return res;
    }
};