class Solution:
    def trap(self, h: List[int]) -> int:
        a=len(h)
        l=[0]*a
        l[0]=h[0]
        for i in range(1,a):
            l[i]=max(l[i-1],h[i])
        r=[0]*a
        r[a-1]=h[a-1]
        for i in range(a-2,-1,-1):
            r[i]=max(h[i],r[i+1])
        res=0
        for i in range(1,a-1):
            k=min(l[i-1],r[i+1])
            if k>h[i]:
                res+=k-h[i]
        return res