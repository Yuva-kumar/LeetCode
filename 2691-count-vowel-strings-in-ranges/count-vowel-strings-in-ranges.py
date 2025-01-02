class Solution:
    def vowelStrings(self, words: List[str], qu: List[List[int]]) -> List[int]:
        l=[0]*(len(words))
        for i in range(len(words)):
            if words[i][0] in "aeiou" and words[i][-1] in "aeiou":
                l[i]=1
        for i in range(1,len(l)):
            l[i]+=l[i-1]
        l=[0]+l
        res=[]
        for i,j in qu:
            res.append(l[j+1]-l[i])
        return res