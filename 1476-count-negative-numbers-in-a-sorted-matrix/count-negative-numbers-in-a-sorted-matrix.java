class Solution {
    public int countNegatives(int[][] grid) {

        int res = 0;

        for(int i =0; i < grid.length; i++){
            for(int index : grid[i]){
                if (index < 0){
                    res++;
                }
            }
        }

        return res;
        
    }
}