class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        a,b,c=-1,-1,-1
        res=0
        for i in range(len(s)):
            if s[i]=='a':
                a=i
            elif s[i]=='b':
                b=i
            else:
                c=i
            res+=1+min(a,b,c)
        return res