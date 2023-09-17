from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.append(item)

    def dequeque(self):
        return self.items.popleft()

    def size(self):
        return len(self.items)

    def peak(self):
        return self.items[0]

    def __str__(self):
        return str(self.items)


if __name__ == "__main__":
    queue = Queue()
    print(queue)
    print(queue.is_empty())
    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")
    queue.enqueue("D")
    print(queue)
    print(queue.is_empty())
    print(queue.dequeque())
    print(queue)
    print(queue.peak())
    print(queue.size())
