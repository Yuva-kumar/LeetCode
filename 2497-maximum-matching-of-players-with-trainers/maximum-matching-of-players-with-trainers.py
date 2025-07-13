class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        
        res = 0
        players.sort()
        trainers.sort()

        for i in range(len(trainers)):

            if res < len(players) and players[res] <= trainers[i]:
                res += 1

        return res
        
        # k = 0
        # while True:

        #     if(len(players) == 0 or len(trainers) == 0):
        #         return res

        #     if(players[0] <= trainers[k]):

        #         trainers.pop(k)
        #         players.pop(0)
        #         res += 1
               
        #     else:
        #         trainers.pop(0)
        # return res