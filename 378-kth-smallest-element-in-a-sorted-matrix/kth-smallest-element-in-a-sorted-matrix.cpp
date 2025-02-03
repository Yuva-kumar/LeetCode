class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {

        priority_queue<int> maxHeap;
        for(auto& it:matrix){
            for(int i:it){
                maxHeap.push(i);
                if(maxHeap.size()>k){
                    maxHeap.pop();
                }
            }
        }
        return maxHeap.top();

    }
};