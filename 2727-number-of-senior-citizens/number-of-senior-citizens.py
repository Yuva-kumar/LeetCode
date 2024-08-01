class Solution:
    def countSeniors(self, de: List[str]) -> int:
        c=0
        for i in de:
            if int(i[11:13])>60:
                c+=1
        return c
        