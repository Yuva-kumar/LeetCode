class Solution {
public:
void fun(int ind,int target,vector<int>can,vector<int>&v1,vector<vector<int>>&v){
    if (target==0){
        v.push_back(v1);
        return;
    }
    for (int i=ind; i<can.size();i++){
        if (i>ind && can[i]==can[i-1]) continue;
        if (can[i]>target) break;
        v1.push_back(can[i]);
        fun(i+1,target-can[i],can,v1,v);
        v1.pop_back();
    }
}
       
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(),candidates.end());
        vector<int>v1;
        vector<vector<int>>v;
        fun(0,target,candidates,v1,v);
        return v;
        
    }
};