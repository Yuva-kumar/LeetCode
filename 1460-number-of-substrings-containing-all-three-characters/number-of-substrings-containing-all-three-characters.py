class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l=[-1,-1,-1]
        c=0
        for i in range(len(s)):
            l[ord(s[i])-97]=i
            c+=1+min(l)
        return c