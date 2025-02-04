class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res,cur=nums[0],nums[0]
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                cur+=nums[i+1]
            else:
                res=max(res,cur)
                cur=nums[i+1]
            res=max(cur,res)
        return res
