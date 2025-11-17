class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:

        l = [i for i in range(len(nums)) if nums[i] == 1]
        for i in range(len(l)-1):
            print(l[i+1]-l[i]-1)
            if l[i+1]-l[i]-1 < k:
                return False
        return True


