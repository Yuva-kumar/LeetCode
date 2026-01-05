class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        res, nc = 0,0
        ps,ns = 2**31,2**31
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(matrix[i][j]) < 0:
                    nc += 1
                    res += matrix[i][j]*-1
                    ns = min(ns,matrix[i][j]*-1)
                else:
                    res += matrix[i][j]
                    ps = min(ps,matrix[i][j])
        if nc%2 == 0:
            return res
        else:
            return res-2*min(ps,ns)
           
