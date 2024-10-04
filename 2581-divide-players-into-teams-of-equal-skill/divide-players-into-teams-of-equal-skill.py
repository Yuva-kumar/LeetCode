class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n=len(skill)
        c,d,e=0,0,0
        for i in range(n//2):
            k1=skill[i]+skill[n-1-i]
            c+=skill[i]*skill[n-1-i]
            if k1!=d:
                e+=1
                d=k1
        if e!=1:return -1
        return c