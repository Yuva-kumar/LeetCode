class Solution:
    def maxSum(self, nums: List[int]) -> int:
        
        if max(nums) < 0:
            return max(nums)
        
        l = [0]*101
        res = 0
        for i in nums:
            if (i >= 0) and (l[i] == 0):
                res += i 
                l[i] = 1
        return res

        