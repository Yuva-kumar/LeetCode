class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        l=[]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                l.append(sum(nums[i:j+1]))
        l.sort()
        # print(l)
        return sum(l[left-1:right])%(10**9+7)
        