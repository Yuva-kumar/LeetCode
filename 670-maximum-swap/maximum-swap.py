class Solution:
    def maximumSwap(self, num: int) -> int:
        if num<10:
            return num
        k=str(num)
        k1=list(k)
        for i in range(1,len(k1)):
            a=k1[i-1]
            b=max(k1[i:])
            if max(a,b)!=a:
                k1[i-1]=b
                x=len(k)-k1[i:][::-1].index(b)-1
                k1[x]=a
                # print(k1)
                break
        res="".join(k1)
        return int(res)