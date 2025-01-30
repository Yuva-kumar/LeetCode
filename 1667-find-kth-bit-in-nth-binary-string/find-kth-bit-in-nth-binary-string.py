class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def fun(s):
            x=""
            for i in s:
                if i=='1':x+='0'
                else:x+='1'
            return s+'1'+x[::-1]
        l=['0']
        for i in range(19):
            a=fun(l[-1])
            l.append(a)
        return l[n-1][k-1]