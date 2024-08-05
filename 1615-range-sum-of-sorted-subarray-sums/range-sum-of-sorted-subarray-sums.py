class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        l=[]
        for i in range(len(nums)):
            s=0
            for j in range(i,len(nums)):
                s+=nums[j]
                l.append(s)
        l.sort()
        # print(l)
        return sum(l[left-1:right])%(10**9+7)
        