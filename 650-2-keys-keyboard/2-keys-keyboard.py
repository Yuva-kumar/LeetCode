class Solution:
    def minSteps(self, n: int) -> int:
        l=[0]*(n+1)
        for i in range(2,n+1):
            if n%i==0:
                l[i]=i
                for j in range(1,i//2+1):
                    if i%j==0:
                        l[i]=min(l[i],i//j+l[j])
        return l[-1]