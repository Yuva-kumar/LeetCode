class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        
        l1,l2 = [],[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] >= 0 :
                    l1.append(matrix[i][j])
                else:
                    l2.append(matrix[i][j]*-1)
        
        l2.sort()
        res = sum(l1)+sum(l2)
        if(len(l2) % 2 ==0):
            return res
        else:
            if(len(l2) == 0):
                return sum(l1)
            elif len(l1) ==0:
                return sum(l2) - 2*min(l2)

            return res-2*min(min(l1),min(l2))
