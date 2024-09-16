class Solution:
    def findMinDifference(self, tp: List[str]) -> int:
        l=[]
        for i in tp:
            a=i.index(':')
            x=i[:a]
            y=i[a+1:]
            if 60*int(x)+int(y)==0:
                l.append(1440)
            else:l.append(60*int(x)+int(y))
        l.sort()
        res=1440
        for i in range(len(l)-1):
            res=min(res,l[i+1]-l[i])
        res=min((1440-l[-1]+l[0]),res)
        return res
