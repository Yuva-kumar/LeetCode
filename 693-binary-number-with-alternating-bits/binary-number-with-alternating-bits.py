class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        k = bin(n)[2:]
        for i in range(len(k)-1):
            if k[i] == k[i+1]:
                return False
        return True