class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        # [a,b,c,d,x]
        # 4
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
            #[b,c,d,x,a] 4
            #[c,d,x,a,b] 3
            #[d,x,a,b,c] 2
            #[x,a,b,c,d] 1

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        if len(self.q): return False
        return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()