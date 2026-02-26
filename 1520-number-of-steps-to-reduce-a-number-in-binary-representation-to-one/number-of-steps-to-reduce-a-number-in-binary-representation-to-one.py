class Solution:
    def numSteps(self, s: str) -> int:

        def fun(n,res):
            if n == 1:
                return res
            if(n%2 == 0):
                return fun(n//2,res+1)
            else:
                return fun(n+1,res+1)
       
        c = 0
        for i in range(len(s)):
            if s[i] == '1':
                c += 2**(len(s)-1-i)
        res = fun(c,0)
        return res