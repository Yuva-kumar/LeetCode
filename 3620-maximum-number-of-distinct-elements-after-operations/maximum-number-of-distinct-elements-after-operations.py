class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        for i in range(len(nums)):
            nums[i]+=k
        nums[0]-=2*k
        x=nums[0]+1
        for i in range(1,len(nums)):
            if x>nums[i]:
                continue
            if nums[i]-2*k >x:
                nums[i]-=2*k
                x=nums[i]+1
            else:
                nums[i]=x
                x+=1
        # print(nums)
        return len(set(nums))
