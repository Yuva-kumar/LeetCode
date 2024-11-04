class Solution:
    def compressedString(self, w: str) -> str:
        l=[]
        a=1
        for i in range(len(w)-1):
            if w[i]==w[i+1]:
                a+=1
            else:
                l.append(a)
                l.append(w[i])
                a=1
        l.append(a)
        l.append(w[-1])
        res=""
        for i in range(0,len(l),2):
            k=l[i]//9
            for j in range(k):
                res+='9'+l[i+1]
            s=l[i]%9
            if s!=0:
                res+=str(s)+l[i+1]

        return res