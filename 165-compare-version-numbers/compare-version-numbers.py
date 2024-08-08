class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        def fun(v):
            l=[]
            a=''
            for i in v:
                if i!='.':
                    a+=i
                else:
                    if len(a)==0:
                        l.append(0)
                    else:
                        l.append(int(a))
                    a=""
            l.append(int(a))
            return l
        a=fun(v1)
        b=fun(v2)
        if len(a)!=len(b):
            k=min(len(a),len(b))
            if k==len(a):
                a=a+[0]*(len(b)-len(a))
            else:
                b=b+[0]*(len(a)-len(b))
        for i in range(len(a)):
            if a[i]>b[i]:
                return 1
            elif b[i]>a[i]:
                return -1
        return 0
