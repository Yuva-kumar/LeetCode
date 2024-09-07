class Solution:
    def isHappy(self, n: int) -> bool:
        def fun(n):
            c=0
            while n:
                r=n%10
                n//=10
                c+=r**2
            return c
        while (n//10 !=0):
            n=fun(n)
        if (n==1 or n==7):return True
        return False
