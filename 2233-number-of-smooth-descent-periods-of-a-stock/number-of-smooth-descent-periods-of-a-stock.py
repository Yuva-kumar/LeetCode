class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:

        res = len(prices)
        c,l = 0,[]
        for i in range(len(prices)-1):
            if (prices[i] - prices[i+1] == 1):
                c += 1
            else:
                l.append(c)
                c = 0
        l.append(c)
        for i in l:
            if i != 0:
                res += (i*(i+1))//2
        # print(l)
        return res
        