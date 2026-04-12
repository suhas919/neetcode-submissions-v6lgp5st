class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append([timestamp,value])
        else:
            self.map[key] = [[timestamp,value]]
        #print(self.map)

    def get(self, key: str, timestamp: int) -> str:
        
        res = ""

        if key not in self.map:
            return res

        n = len(self.map[key])

        l = 0
        r = n-1

        while l <= r:
            m = (l+r)//2
            print(m,self.map[key][m])
            if timestamp >= self.map[key][m][0]:
                res = self.map[key][m][1]
                l = m+1
            else:
                r = m-1

        return res
