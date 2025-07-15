class Solution {
    public boolean isValid(String word) {

        if(word.length() < 3) return false;
        int oc = 0;
        int cc = 0;

        for(char ch : word.toCharArray()){

               if(!Character.isLetter(ch) && !Character.isDigit(ch)){
                return false;
               }

               char i = Character.toLowerCase(ch);
               
               if( i == 'a' | i == 'e' | i == 'i' | i == 'o' | i == 'u'){
                oc += 1;
               }else if( !Character.isDigit(i)){
                cc += 1;
               }

        }
        
        if(oc == 0 | cc == 0 ){
            return false;
        }
        return true;
        
    }
}