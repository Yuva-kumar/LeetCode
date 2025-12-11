class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:

        x_cor = buildings.copy()
        x_cor.sort()
        y_cor = [[i[1],i[0]] for i in buildings]
        y_cor.sort()

        def checking_cor(cor):
            s = {}
            for i in cor:
                if i[0] not in s:
                    s[i[0]] = []
                s[i[0]].append(i)
            return s

        def slicing_cor(xy_data):
            l = []
            for i in xy_data:
                if len(xy_data[i]) >= 3:
                    l.extend(xy_data[i][1:-1])
            return l
        
        x_data = checking_cor(x_cor)
        y_data = checking_cor(y_cor)

        # print(x_data,y_data)

        x_slicing_data = slicing_cor(x_data)
        y_slicing_data = slicing_cor(y_data)

        # print(x_slicing_data,y_slicing_data)

        if(len(x_slicing_data) == 0 or len(y_slicing_data) == 0):
            return 0
        
        res1,res2 = 0,0

        final_dict = {}
        for i in x_slicing_data:
            c = str(i[1])+ "*" + str(i[0])
            if c not in final_dict:
                final_dict[c] = 1
            else:
                final_dict[c] += 1
        for i in y_slicing_data:
            c = str(i[0])+ "*" + str(i[1])
            if c not in final_dict:
                final_dict[c] = 1
            else:
                final_dict[c] += 1

        for i in final_dict:
            if final_dict[i] > 1:
                res1 += 1
        

        # for i in x_slicing_data:
        #     k = [i[1],i[0]]
        #     if k in y_slicing_data:
        #         res += 1


        return res1