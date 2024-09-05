class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        a=sum(rolls)
        k=len(rolls)+n
        x=(k*mean)-a
        if x> (6*n) or x<0 or x<n :return []
        else:
            res=[x//n]*n
            k=x-sum(res)
            i=0
            while k!=0:
                res[i]+=1
                i+=1
                k-=1
            return res



        