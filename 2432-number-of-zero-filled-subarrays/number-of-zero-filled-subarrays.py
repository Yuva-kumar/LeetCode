class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:

        i,c,res = 0,0,0

        while i < len(nums):

            if nums[i] == 0:
                c += 1
            else:
                res += (c*(c+1))//2
                c = 0

            i += 1
            
        res += (c*(c+1))//2

        return res