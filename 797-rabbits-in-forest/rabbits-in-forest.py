class Solution:
    import math
    def numRabbits(self, answers: List[int]) -> int:

        s = {}
        for i in answers:
            if i not in s:
                s[i] = 1
            else:
                s[i] += 1
        res = 0
        for i in s:
            res += (i+1)*(math.ceil(s[i]/(i+1)))
        return res
               