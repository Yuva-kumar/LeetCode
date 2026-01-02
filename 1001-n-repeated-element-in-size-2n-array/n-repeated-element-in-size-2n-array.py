class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        
        n = len(nums)//2

        s = {}
        for i in nums:
            if i not in s:
                s[i] = 1
            else:
                s[i] += 1
        for i in s:
            if s[i] == n:
                return i