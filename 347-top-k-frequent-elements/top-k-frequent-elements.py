class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s={}
        for i in nums:
            if i not in s:
                s[i]=1
            else:
                s[i]+=1
        l=[]
        for i in s:
            a=(s[i],i)
            l.append(a)
        l.sort(reverse=True)
        res=[]
        for i in range(k):
            res.append(l[i][1])
        return res