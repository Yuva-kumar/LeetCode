class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        a=set()
        b=set()
        c,l=0,[]
        for i in range(len(A)):
            a.add(A[i])
            b.add(B[i])
            if(A[i]==B[i]):
                c+=1
            else:
                if(A[i] in b):
                    c+=1
                if(B[i] in a):
                    c+=1
            l.append(c)
        return l