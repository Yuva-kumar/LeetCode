class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res=""
        k=0
        i=0
        for j in s:
            if i==len(spaces):
                break
            if k==spaces[i]:
                res+=" "
                i+=1
            k+=1
            res+=j
            
        return res+s[spaces[-1]+1:]