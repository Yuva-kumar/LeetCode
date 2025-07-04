class Solution:
    def checkPowersOfThree(self, n: int) -> bool:

        def fun(num):
            k = int(num**(1/3))
            while 3 ** k > num:
                k -= 1  
            diff = num - 3**k
            return diff, k

        temp = n
        power = set()

        while True:
            if temp == 0:
                return True

            diff, k = fun(temp)

            if k in power:
                return False  

            power.add(k)
            temp = diff

    