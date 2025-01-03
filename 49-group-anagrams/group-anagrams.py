class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def fun(n):
            n=sorted(n)
            return "".join(n)
        l=[]
        for i in strs:
            a=(fun(i),i)
            l.append(a)
        l.sort()
        s={}
        for i in l:
            if i[0] not in s:
                s[i[0]]=1
            else:
                s[i[0]]+=1
        k=s.values()
        x=0
        res=[]
        for i in k:
            r=[]
            for j in range(i):
                r.append(l[x][1])
                x+=1
            res.append(r)
        return res
                

        return [[]]