class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        while True:
            c=0
            for i in range(len(nums)-1):
                a=bin(nums[i])
                b=bin(nums[i+1])
                if ((a.count('1'))==(b.count('1'))) and (nums[i]>nums[i+1]):
                    nums[i],nums[i+1]=nums[i+1],nums[i]
                    c+=1
            if c==0:
                break
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:return False
        return True