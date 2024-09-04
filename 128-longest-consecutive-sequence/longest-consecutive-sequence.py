class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:return 0
        c,d=0,0
        nums=list(set(nums))
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]==1:
                c+=1
            else:
                c=0
            d=max(c,d)
        return d+1
