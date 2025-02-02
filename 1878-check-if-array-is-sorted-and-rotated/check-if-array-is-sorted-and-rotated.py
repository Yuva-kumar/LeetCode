class Solution:
    def check(self, nums: List[int]) -> bool:
        def fun(x):
            x.sort()
            return x
        l=nums
        for i in range(len(nums)):
            l=[l[-1]]+l[:-1]
            l1=l.copy()
            if l==fun(l1):
                return True
        return False


