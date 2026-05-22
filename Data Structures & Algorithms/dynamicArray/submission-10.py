class DynamicArray:

    def __init__(self, capacity: int):

        assert capacity > 0, "Capacity cannot be <= 0"

        self.arr = [0] * capacity
        self.capacity = capacity
        self.length = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.length += 1
        self.arr[self.length - 1] = n


    def popback(self) -> int:
        self.length -= 1
        return self.arr[self.length]

    def resize(self) -> None:
        tempArr = [0] * self.capacity
        self.capacity *= 2
        self.arr += tempArr

    def getSize(self) -> int:
        return self.length

    def getCapacity(self) -> int:
        return self.capacity

    
