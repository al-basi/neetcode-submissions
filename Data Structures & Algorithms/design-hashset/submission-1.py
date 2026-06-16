class MyHashSet:

    def __init__(self):
        self.mem = []

    def add(self, key: int) -> None:
        if key not in self.mem:
            self.mem.append(key)

    def remove(self, key: int) -> None:
        try:
            self.mem.remove(key)
        except:
            pass

    def contains(self, key: int) -> bool:
        return key in self.mem


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)