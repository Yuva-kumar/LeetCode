class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        c,d=1,1
        x,y=1,1
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                c+=1
            else:
                c=1
            x=max(c,x)
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                d+=1
            else:
                d=1
            y=max(d,y)
        return max(x,y)