class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        l=[0]*(10**5)
        for i in grid:
            for j in i:
                l[j]+=1
        a,b=0,0
        for i in range(len(l)):
            if l[i]==2:
                a=i
            if l[i]==0:
                b=i
            if a!=0 and b!=0:
                return [a,b]