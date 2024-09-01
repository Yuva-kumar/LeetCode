class Solution:
    def construct2DArray(self, orl: List[int], m: int, n: int) -> List[List[int]]:

        l=[]
        if n*m!=len(orl):return l
        for i in range(0,len(orl),n):
            a=orl[i:n+i]
            l.append(a)
        return l

        