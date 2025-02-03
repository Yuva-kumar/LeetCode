class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        s={}
        for i in words:
            if i not in s:
                s[i]=1
            else:
                s[i]+=1
        l=[]
        for i in s:
            a=(i,s[i])
            l.append(a)
        l1= sorted(l,key= lambda x: (-x[1],x[0]))
        res=[]
        for i in range(k):
            res.append(l1[i][0])
        return res