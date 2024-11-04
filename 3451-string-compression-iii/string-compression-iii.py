class Solution:
    def compressedString(self, w: str) -> str:
        l=[]
        a=1
        for i in range(len(w)-1):
            if w[i]==w[i+1]:
                if a==9:
                    l.append(9)
                    l.append(w[i])
                    a=0
                a+=1
            else:
                l.append(a)
                l.append(w[i])
                a=1
        l.append(a)
        l.append(w[-1])
        res=""
        for i in range(0,len(l),2):
            res+=str(l[i])+l[i+1]
        return res
      