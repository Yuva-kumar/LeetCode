class Solution {
    public int maximumCount(int[] nums) {

        int posNum = 0;
        int negNum = 0;

        for(int item : nums){
            if(item < 0){
                negNum++;
            }
            else if( item > 0){
                posNum++;
            }
        }

        return Math.max(posNum,negNum);
        
    }
}