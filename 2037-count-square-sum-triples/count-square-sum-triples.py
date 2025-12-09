class Solution:
    def countTriples(self, n: int) -> int:
        
        count = 0
        for i in range(1,n):
            for j in range(2,n):
                sqrt = (i**2+j**2)**0.5
                if(int(sqrt) == sqrt) and int(sqrt) <= n:
                    count += 1
        return count