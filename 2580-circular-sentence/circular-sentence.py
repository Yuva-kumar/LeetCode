class Solution:
    def isCircularSentence(self, se: str) -> bool:
        k=se.split()
        for i in range(len(k)-1):
            if k[i][-1]!=k[i+1][0]:
                return False
        if k[-1][-1]==k[0][0]:
            return True
        return False