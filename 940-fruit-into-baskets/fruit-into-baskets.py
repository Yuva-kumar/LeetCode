class Solution:
    def totalFruit(self, frs: List[int]) -> int:
        l,r,res=0,0,0
        s={}
        while r<len(frs):
            if frs[r] not in s:
                s[frs[r]]=1
            else:
                s[frs[r]]+=1
            if len(s)>2:
                s[frs[l]]-=1
                if s[frs[l]]==0:
                    del s[frs[l]]
                l+=1
            res=max(res,r-l+1)
            r+=1
        print(s)
        return res
        