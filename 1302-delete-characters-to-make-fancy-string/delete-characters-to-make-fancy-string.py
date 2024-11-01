class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s)<3:return s
        l=[s[0],s[1]]
        for i in range(2,len(s)):
            if l[-1]!=s[i] or l[-2]!=s[i]:
                l.append(s[i])
        # print(l)
        return "".join(l)