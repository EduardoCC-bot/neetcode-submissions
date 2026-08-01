class FreqStack:

    def __init__(self):
        self.stack = []
        self.mapa  = defaultdict(int)
        self.index = 0

    def push(self, val: int) -> None:
        self.mapa[val] += 1
        heapq.heappush(self.stack, (-self.mapa[val], -self.index, val))
        self.index += 1

    def pop(self) -> int:
        _,_,val = heapq.heappop(self.stack)
        self.mapa[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()