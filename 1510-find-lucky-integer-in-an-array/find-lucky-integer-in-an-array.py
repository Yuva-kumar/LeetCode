class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        s = {}
        for i in arr:
            if i not in s:
                s[i] = 1
            else:
                s[i] += 1
        res = -1
        for i in s:
            if i == s[i]:
                res = max(i,res)
        return res