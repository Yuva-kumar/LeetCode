class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        l = [i for i in range(len(nums))]
        l1 = list(zip(nums,l))
        l1.sort(reverse = True)
        l1 = l1[:k]
        l2 = []
        for i in l1:
            a = (i[1],i[0])
            l2.append(a)
        l2.sort()
        res = []
        for i in l2:
            res.append(i[1])
        return res

     
