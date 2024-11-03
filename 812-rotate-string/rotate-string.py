class Solution:
    def rotateString(self, s: str, goal: str) -> bool:

        for i in range(len(goal)):
            k=""
            if goal==s:
                return True
            k=goal[-1]+goal[:-1]
            goal=k
        return False