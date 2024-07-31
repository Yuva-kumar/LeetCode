class Solution:
    def countAndSay(self, n: int) -> str:
        def fun(a):
            c=""
            k=1
            for i in range(len(a)-1):
                if i+1!=len(a)-1:
                    if a[i]==a[i+1]:
                        k+=1
                    else:
                        c+=str(k)
                        c+=a[i]
                        k=1
                else:
                    if a[-1]==a[-2]:
                        c+=str(k+1)
                    else:
                        c+=str(k)
                    c+=a[i]
                    k=1
            if a[-1]!=a[-2]:
                c+='1'
                c+=a[-1]
            return c
        l=['1','11']
        for i in range(n-1):
            a=l[-1]
            k=fun(a)
            l.append(k)
        return l[n-1]     