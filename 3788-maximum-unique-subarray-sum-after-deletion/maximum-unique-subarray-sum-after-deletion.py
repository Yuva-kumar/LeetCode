class Solution:
    def maxSum(self, nums: List[int]) -> int:
        

        if max(nums) < 0:
            return max(nums)
        
        l = []
        for i in nums:
            if i >= 0:
                if i not in l:
                    l.append(i)
        return sum(l)