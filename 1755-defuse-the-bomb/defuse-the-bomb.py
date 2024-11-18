class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:

        if k==0:
            return [0]*len(code)
        elif k>0:
            d=code+code
            res=[]
            for i in range(len(code)):
                res.append(sum(d[i+1:i+1+k]))
            return res
        else:
            res=[]
            for i in range(len(code)):
                a=code[:i][::-1]+code[i+1:][::-1]
                res.append(sum(a[:abs(k)]))
            return res
