class Solution {
public:
    vector<int> missingRolls(vector<int>& rolls, int mean, int n) {
        long long s= accumulate(rolls.begin(),rolls.end(),0);
        int k= rolls.size()+n;
        int x= (k*mean)-s;
        vector<int>v;
        if (x<0 || x<n || x>(6*n)){
            return v;
        }
        else{
            int a=x/n;
            vector<int>res(n,a);
            int rem=x-(a*n);
            int i=0;
            while (rem!=0){
                res[i]++;
                rem--;
                i++;
            }
            return res;
        }
    }
};