class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s={}
        for i in arr:
            if i not in s:
                s[i]=1
        k=list(s.keys())
        k.sort()
        d={}
        for i in range(len(k)):
            d[k[i]]=i+1
        res=[]
        for i in arr:
            res.append(d[i])
        return res