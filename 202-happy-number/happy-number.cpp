class Solution {
public:
long long fun(int n){
    long long c=0;
    while (n){
        int r=n%10;
        n/=10;
        c+=r*r;
    }
    return c;

}
    bool isHappy(int n) {

        while (n/10 !=0){
            n=fun(n);
        }
        return (n==1 or n==7);
    }
};