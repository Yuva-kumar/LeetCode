class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        k=sum(nums)
        c,res=0,0
        for i in range(len(nums)-1):
            c+=nums[i]
            if c>=(k-c):
                res+=1
        return res
