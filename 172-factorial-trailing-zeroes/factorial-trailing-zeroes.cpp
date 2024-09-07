class Solution {
public:
    int trailingZeroes(int n) {
        int c=0;
        for(int i=5;i<=n+1;i*=5){
            int k=n/i;
            if (k!=0){
                c+=k;
            }
            else{
                break;
            }
        }
        return c;
        
    }
};