class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res=[]
        k=0
        for i in spaces:
            res.append(s[k:i])
            k=i
        res.append(s[spaces[-1]:])
        # print(res)
        return " ".join(res)