class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = [0] * k
        self.head = -1
        self.tail = -1
        self.max = k

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = 0
        self.tail = (self.tail+1) % self.max
        self.queue[self.tail] = value
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        if self.head == self.tail:
            self.head = self.tail = -1
            return True
        else:
            self.head = (self.head + 1) % self.max
            return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.head % self.max]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.tail % self.max]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        if self.head == -1:
            return True

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        if (self.tail+1)%self.max == self.head%self.max:
        # if len(self.queue) == self.max:
            return True
        else:
            return False


if __name__ == '__main__':
    obj = MyCircularQueue(3)
    print(obj.enQueue(5))
    print(obj.enQueue(2))
    print(obj.enQueue(6))
    print(obj.enQueue(7))
    print(obj.isFull())
    print(obj.Rear())
    print(obj.deQueue())
