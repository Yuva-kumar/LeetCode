class Solution:
    def findComplement(self, num: int) -> int:
        k=bin(num)[2:][::-1]
        d=0
        for i in range(len(k)):
            if k[i]=='0':
                d+=2**i
        return d
        
        