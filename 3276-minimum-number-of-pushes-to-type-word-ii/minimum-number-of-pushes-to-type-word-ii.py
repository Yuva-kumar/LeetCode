class Solution:
    def minimumPushes(self, word: str) -> int:
        s={}
        for i in word:
            if i not in s:
                s[i]=1
            else:
                s[i]+=1
        s=list(s.values())
        s.sort(reverse=True)
        sum=0
        k=0
        for i in s:
           sum+=i*(k//8 +1)
           k+=1
        return sum
        
        