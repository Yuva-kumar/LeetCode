class Solution:
    def digitCount(self, num: str) -> bool:
        
        s = {}
        for i in range(len(num)):
            if i not in s:
                s[i] = 0
            if int(num[i]) not in s:
                s[int(num[i])] = 1
            else:
                s[int(num[i])] += 1

        # print(s)

        for i in range(len(num)):

            if s[i] != int(num[i]):
                return False

        return True