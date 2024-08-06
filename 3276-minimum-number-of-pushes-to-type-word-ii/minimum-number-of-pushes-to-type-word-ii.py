class Solution:
    def minimumPushes(self, word: str) -> int:
        s={}
        for i in word:
            if i not in s:
                s[i]=1
            else:
                s[i]+=1
        s= {key: value for key, value in sorted(s.items(), key=lambda item: item[1], reverse=True)}
        sum=0
        k=0
        for i in s:
           sum+=s[i]*(k//8 +1)
           k+=1
          
        return sum
        
        