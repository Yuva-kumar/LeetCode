class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        res = 10**4+1
        for i in range(len(nums)):
            if nums[i] == target:
                res = min(abs(i-start),res)
        return res