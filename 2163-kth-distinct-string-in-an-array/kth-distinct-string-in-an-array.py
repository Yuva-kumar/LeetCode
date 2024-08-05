class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        s={}
        for i in arr:
            if i not in s:
                s[i]=1
            else:
                s[i]+=1
        l=[]        
        for i in s:
            if s[i]==1:
                l.append(i)
        if len(l)<k:
            return ""
        return l[k-1]