class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        
        l = [nums[0]]
        res = 0

        for i in range(1,len(nums)):
            if (nums[i] != l[-1]):
                l.append(nums[i])

        

        for i in range(len(l)-2):

            if(l[i] > l[i+1] and l[i+2] > l[i+1]) or (l[i+1] > l[i] and l[i+1] > l[i+2]):
                res += 1

        return res
        

