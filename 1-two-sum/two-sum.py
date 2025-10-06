class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i in range(len(nums)):
            s[nums[i]] = i

        for i in range(len(nums)):
            
            if (target-nums[i]) in nums and i!=s[target-nums[i]]:
                return [i,s[target-nums[i]]]
        return -1