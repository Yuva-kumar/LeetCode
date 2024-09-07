class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        def fun(n):
            l=[]
            k=str(int(n)+1)
            for i  in k:
                l.append(int(i))
            return l
        k=""
        for i in digits:
            k+=str(i)
        return fun(k)