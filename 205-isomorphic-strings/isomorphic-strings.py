class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s1,s2={},{}
        for i in range(len(s)):
            if s[i] not in s1:
                s1[s[i]]=1
            else:
                s1[s[i]]+=1
            
            if t[i] not in s2:
                s2[t[i]]=1
            else:
                s2[t[i]]+=1
            
            x=list(s1.values())
            y=list(s2.values())
            # print(x,y)
            if x!=y:
                return False
        return True