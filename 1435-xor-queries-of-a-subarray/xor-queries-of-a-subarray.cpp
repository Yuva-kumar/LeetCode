class Solution {
public:
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& que) {
        vector<int>v;
        for(int i=0;i<que.size();i++){
            long long k=0;
            for(int j=que[i][0];j<=que[i][1];j++){
                k^=arr[j];
            }
            v.push_back(k);
        }
        return v;

    }
};