class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l=[]
        for i in arr:
            a=(abs(x-i),i)
            l.append(a)
        l.sort()
        res=[]
        for i in range(k):
            res.append(l[i][1])
        res.sort()
        return res
        return []
