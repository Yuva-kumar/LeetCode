class Solution:
    def fractionAddition(self, ex: str) -> str:
        import math
        l,l1=[],[]
        s=""
        for i in ex:
            if i in "/+-":
                if len(s)!=0:
                    l.append(int(s))
                l1.append(i)
                s=""
            else:
                s+=i
        l.append(int(s))
        if l1[0]=='/':
            l1=['+']+l1
        l1=[l1[i] for i in range(len(l1)) if i%2==0]
        dum=[l[i] for i in range(len(l)) if i%2==0]
        for i in range(len(l1)):
            if l1[i]=='-':
                dum[i]*=-1
        c=0
        for i in range(len(l)):
            if i%2==0:
                l[i]=dum[c]
                c+=1
        a,b=0,1
        for i in range(0,len(l),2):
            c,d=l[i],l[i+1]
            a=(a*d)+(b*c)
            b=b*d
        if a==0:return(str(a)+'/'+'1')
        k=math.gcd(a,b)
        return str(a//k)+'/'+str(b//k)