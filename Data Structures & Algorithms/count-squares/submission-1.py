class CountSquares:

    def __init__(self):
        self.mapa = defaultdict(int)    

    def add(self, point: List[int]) -> None:
        self.mapa[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        qx = point[0]
        qy = point[1]
        res = 0
        for x, y in self.mapa.keys():
            if x != qx and y != qy and abs(x - qx) == abs(y - qy) and (x, qy) in self.mapa and (qx, y) in self.mapa:
                res += self.mapa[(x,qy)] * self.mapa[(qx,y)] * self.mapa[(x,y)] 
        return res

