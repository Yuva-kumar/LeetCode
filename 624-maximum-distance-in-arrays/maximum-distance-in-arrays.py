class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        l,l1=[],[]
        for i in arrays:
            l.append(i[0])
            l1.append(i[-1])
        a=l.index(min(l))
        b=l1.index(max(l1))
        if a==b:
            k=l1[:b]+l1[b+1:]
            k1=max(k)-min(l)
            k2=l[:a]+l[a+1:]
            k3=max(l1)-min(k2)
            return max(k1,k3)
        else:
            return max(l1)-min(l)


        
        