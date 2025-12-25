class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)
        c,res = 0,0
        for i in range(k):
            if(happiness[i] - c) > 0:
                res += happiness[i] - c
                c += 1
        # print(res)
        return res

        