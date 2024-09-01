class Solution:
    def construct2DArray(self, orl: List[int], m: int, n: int) -> List[List[int]]:

        l=[]
        if n*m!=len(orl):return l
        for i in range(m):
            l1=[]
            for j in range(n):
                l1.append(orl[j])
            orl=orl[n:]
            l.append(l1)
        return l

        