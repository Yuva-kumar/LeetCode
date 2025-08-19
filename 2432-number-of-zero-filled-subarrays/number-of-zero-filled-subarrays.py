class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        l = []
        i,c = 0,0
        while i < len(nums):

            if nums[i] == 0:
                c += 1
            else:
                l.append(c)        
                c = 0
            i += 1
        l.append(c)
        res = 0
        for i in l:
            res += (i*(i+1))//2

        return res