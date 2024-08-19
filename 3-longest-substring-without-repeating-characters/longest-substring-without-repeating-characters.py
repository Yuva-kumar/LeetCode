class Solution:
    def lengthOfLongestSubstring(self, arr: str) -> int:
        if len(arr)==0:
            return 0
        d=[-1]*256
        l,r=0,0
        res=0
        while r<len(arr):
            if d[ord(arr[r])]!=-1:
                if d[ord(arr[r])]>=l:
                    l=d[ord(arr[r])]+1
            d[ord(arr[r])]=r
            r+=1
            res=max(res,r-l+1)
        return res-1