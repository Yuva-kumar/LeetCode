class Solution {
public:
    long long maxKelements(vector<int>& nums, int k) {
        long long res=0;
        priority_queue<long long> maxHeap(nums.begin(),nums.end());
        while (k--){
            long long x=maxHeap.top();
            maxHeap.pop();
            res+=x;
            long long a=ceil(x/3.0);
            maxHeap.push(a);
        }
        return res;
    }
};