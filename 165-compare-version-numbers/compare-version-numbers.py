class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        a=v1.split('.')
        b=v2.split('.')
        if len(a)!=len(b):
            k=min(len(a),len(b))
            if k==len(a):
                a=a+[0]*(len(b)-len(a))
            else:
                b=b+[0]*(len(a)-len(b))
        for i in range(len(a)):
            if int(a[i])>int(b[i]):
                return 1
            elif int(b[i])>int(a[i]):
                return -1
        return 0
