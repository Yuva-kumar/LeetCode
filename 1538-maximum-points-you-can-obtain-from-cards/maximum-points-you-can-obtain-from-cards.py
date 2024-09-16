class Solution:
    def maxScore(self, ca: List[int], k: int) -> int:
        l,r,res=sum(ca[:k]),0,sum(ca[:k])
        a=len(ca)-1
        for i in range(k-1,-1,-1):
            l-=ca[i]
            r+=ca[a]
            res=max(res,l+r)
            a-=1
        return res


