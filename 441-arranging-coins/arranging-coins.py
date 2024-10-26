class Solution:
    def arrangeCoins(self, n: int) -> int:
        # if n==1:return 1
        k=1
        while True:
            if (k*(k+1))//2 >n:
                break
            k+=1
        return k-1