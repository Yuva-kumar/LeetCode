class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        c = 0
        for i in range(1,len(nums)):
            if(abs(sum(nums[:i])-sum(nums[i:]))) %2 == 0:
                c += 1
        return c
        