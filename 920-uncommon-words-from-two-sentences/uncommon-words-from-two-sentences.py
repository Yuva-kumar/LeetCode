class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1=s1.split(' ')
        s2=s2.split(' ')
        k=s1+s2
        s={}
        for i in k:
            if i not in s:
                s[i]=1
            else:
                s[i]+=1
        res=[]
        for i in s:
            if s[i]==1:
                res.append(i)
        return res