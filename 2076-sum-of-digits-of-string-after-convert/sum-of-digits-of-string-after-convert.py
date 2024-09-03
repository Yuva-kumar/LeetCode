class Solution:
    def getLucky(self, s: str, k: int) -> int:
        k1=''
        for i in s:
            k1+=str(ord(i)-96)
        c=0
        while k!=0:
            for i in k1:
                c+=int(i)
            k1=str(c)
            c=0
            k-=1
        return int(k1)
            