import java.util.HashMap;


class Solution {

    public int numRabbits(int[] answers) {

        int res = 0;

        HashMap<Integer,Integer> map = new HashMap();

        for(int num : answers){
            map.put(num, map.getOrDefault(num,0)+1);
        }
        
        for(int key : map.keySet()){
            
            int rabbits = (int) Math.ceil((double) map.get(key)/(key+1));
            res += (key+1)*(rabbits);
        }

        return res;
        

    }
}