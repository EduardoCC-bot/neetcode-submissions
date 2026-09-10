class MyHashSet:

    def __init__(self):
        self.mapa = set()

    def add(self, key: int) -> None:
        self.mapa.add(key)

    def remove(self, key: int) -> None:
        if key in self.mapa:
            self.mapa.remove(key)

    def contains(self, key: int) -> bool:
        if key in self.mapa:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)