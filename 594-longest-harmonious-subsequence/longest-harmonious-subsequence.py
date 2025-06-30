class Solution:
    def findLHS(self, nums: List[int]) -> int:
        s = {}
        for i in nums:
            if i not in s:
                s[i] = 1
            else:
                s[i] += 1
        s = sorted(s.items())
        res = 0
        for i in range(len(s)-1):
            if abs(s[i][0]-s[i+1][0]) == 1:
                res = max(res,s[i+1][1]+s[i][1])
        return res