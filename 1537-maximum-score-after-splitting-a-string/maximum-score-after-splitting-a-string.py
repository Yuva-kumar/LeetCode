class Solution:
    def maxScore(self, s: str) -> int:
        
        res=0
        for i in range(1,len(s)):
            x=s[:i]
            y=s[i:]
            res=max(res,x.count('0')+y.count('1'))
        return res