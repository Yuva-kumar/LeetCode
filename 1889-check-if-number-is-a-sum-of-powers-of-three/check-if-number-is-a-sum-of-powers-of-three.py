class Solution:
    def checkPowersOfThree(self, n: int) -> bool:



        def fun(num):
            k = 0
            while 3**k <= num:
                k+=1
            k-=1
            
            diff = abs(num - 3**k)
            return diff, k

        temp = n
        while True:
            if temp == 0 or temp == 1 :
                return True

            if temp == 2: 
                return False

            diff, k = fun(temp)

            if (diff >= 3**k):
                return False

            temp = diff

        