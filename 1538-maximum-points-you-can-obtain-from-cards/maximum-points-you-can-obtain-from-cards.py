class Solution:
    def maxScore(self, ca: List[int], k: int) -> int:
        def fun(ca,k):
            a=sum(ca[:k])
            l=[a]
            for i in range(k-1,-1,-1):
                l.append(l[-1]-ca[i])
            return l
        a=fun(ca,k)
        b=fun(ca[::-1],k)
        res=0
        for i in range(k+1):
            res=max(res,a[i]+b[k-i])
        # print(res)
        return res

